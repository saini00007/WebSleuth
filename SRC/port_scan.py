from scapy.all import *
from urllib.parse import urlparse
import socket
import sys
def get_domain_from_url(url):
    parsed_uri = urlparse(url)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    return domain

def get_open_ports(ip):
    open_ports = []
    ports_range = range(1, 1025)
    
    responses, _ = sr(IP(dst=ip)/TCP(dport=ports_range, flags="S"), timeout=1, verbose=False)
    
    for response in responses:
        if response[1].haslayer(TCP) and response[1][TCP].flags == 18: # SYN-ACK
            open_ports.append(response[1][TCP].sport)
    return open_ports

def colorize(text, color):
    colors = {
        "red": "\033[31m",
        "green": "\033[32m",
        "blue": "\033[34m",
        "reset": "\033[0m"
        
    }
    return f"{colors[color]}{text}{colors['reset']}"

url = sys.argv[1]
domain = get_domain_from_url(url)
ip = socket.gethostbyname(domain)
open_ports = get_open_ports(ip)
print("====================")
print(colorize( "  Open_ports ", "blue",))

print("====================\n")
    

print(colorize("Open ports Number:", "red"))
for port in open_ports:
    print(colorize(port, "green"))
print("\n")  
