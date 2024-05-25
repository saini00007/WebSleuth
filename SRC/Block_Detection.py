import socket
import ipaddress
from urllib.parse import urlparse
from typing import List, Dict
import sys

# ANSI escape codes for colorization
GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

DNS_SERVERS = [
    {'name': 'AdGuard', 'ip': '176.103.130.130'},
    {'name': 'AdGuard Family', 'ip': '176.103.130.132'},
    {'name': 'CleanBrowsing Adult', 'ip': '185.228.168.10'},
    {'name': 'CleanBrowsing Family', 'ip': '185.228.168.168'},
    {'name': 'CleanBrowsing Security', 'ip': '185.228.168.9'},
    {'name': 'CloudFlare', 'ip': '1.1.1.1'},
    {'name': 'CloudFlare Family', 'ip': '1.1.1.3'},
    {'name': 'Comodo Secure', 'ip': '8.26.56.26'},
    {'name': 'Google DNS', 'ip': '8.8.8.8'},
    {'name': 'Neustar Family', 'ip': '156.154.70.3'},
    {'name': 'Neustar Protection', 'ip': '156.154.70.2'},
    {'name': 'Norton Family', 'ip': '199.85.126.20'},
    {'name': 'OpenDNS', 'ip': '208.67.222.222'},
    {'name': 'OpenDNS Family', 'ip': '208.67.222.123'},
    {'name': 'Quad9', 'ip': '9.9.9.9'},
    {'name': 'Yandex Family', 'ip': '77.88.8.7'},
    {'name': 'Yandex Safe', 'ip': '77.88.8.88'},
]

KNOWN_BLOCK_IPS = [
    '146.112.61.106', '185.228.168.10', '8.26.56.26', '9.9.9.9', '208.69.38.170', '208.69.39.170', '208.67.222.222',
    '208.67.222.123', '199.85.126.10', '199.85.126.20', '156.154.70.22', '77.88.8.7', '77.88.8.8', '::1',
    '2a02:6b8::feed:0ff', '2a02:6b8::feed:bad', '2a02:6b8::feed:a11', '2620:119:35::35', '2620:119:53::53',
    '2606:4700:4700::1111', '2606:4700:4700::1001', '2001:4860:4860::8888', '2a0d:2a00:1::', '2a0d:2a00:2::'
]


def is_domain_blocked(domain: str, server_ip: str) -> bool:
    try:
        addresses = socket.gethostbyname_ex(domain)[-1]
        for addr in addresses:
            if addr in KNOWN_BLOCK_IPS:
                return True
        return False
    except socket.gaierror as e:
        try:
            addresses6 = socket.getaddrinfo(domain, None, socket.AF_INET6)
            for addr_info in addresses6:
                addr = ipaddress.ip_address(addr_info[4][0])
                if str(addr) in KNOWN_BLOCK_IPS:
                    return True
            return False
        except (socket.gaierror, socket.herror) as e:
            if e.errno in (socket.EAI_NONAME, socket.EAI_NODATA, socket.EAI_FAIL):
                return True
            return False


def check_domain_against_dns_servers(domain: str) -> List[Dict[str, str]]:
    results = []
    for server in DNS_SERVERS:
        is_blocked = is_domain_blocked(domain, server['ip'])
        result_text = f"{GREEN}YES{RESET}" if is_blocked else f"{BLUE}NO{RESET}"
        results.append({'server': server['name'], 'isBlocked': result_text})
    return results


def handler(url: str) -> Dict[str, List[Dict[str, str]]]:
    domain = urlparse(url).hostname
    results = check_domain_against_dns_servers(domain)
    return {'blocklists': results}


if __name__ == "__main__":
    
    
    try:
        url = sys.argv[1]
        
        result = handler(url)
        print("====================")
        print(BLUE + "Block Detection " + RESET)
        print("====================\n")
        print("\nDNS Servers              Blocked")
        print("-----------------------------------")
        for res in result['blocklists']:
            print(RED + f"{res['server']:25} {res['isBlocked']:>7}")
        print("\n")
    except Exception as e:
        print(f"\n{RED}Error: {e}{RESET}")
