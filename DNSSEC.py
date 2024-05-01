import requests
from colorama import Fore, Style

def handler(domain):
    dns_types = ['DNSKEY', 'DS', 'RRSIG']
    records = {}

    for dns_type in dns_types:
        url = f"https://dns.google/resolve?name={domain}&type={dns_type}"
        headers = {'Accept': 'application/dns-json'}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            dns_response = response.json()

            records[dns_type] = {
                'isFound': bool(dns_response.get('Answer')),
                'answer': dns_response.get('Answer', []),
                'flags': dns_response.get('AD'),
            }
        except Exception as error:
            raise Exception(f"Error fetching {dns_type} record: {error}")

    return records

def print_dns_records(records):
    for dns_type, record in records.items():
        print(f"{Fore.RED}{dns_type}{Style.RESET_ALL}")
        print(f"{Fore.RED}{dns_type} - Present? {'✅ Yes' if record['isFound'] else '❌ No'}{Style.RESET_ALL}")
        print()
        print(f"{Fore.BLUE}    Recursion Desired (RD)✅{Style.RESET_ALL}")
        print(f"{Fore.BLUE}    Recursion Available (RA)✅{Style.RESET_ALL}")
        print(f"{Fore.BLUE}    TrunCation (TC)❌{Style.RESET_ALL}")
        print(f"{Fore.BLUE}    Authentic Data (AD) {'✅' if record['flags'] else '❌'}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}    Checking Disabled (CD)❌{Style.RESET_ALL}")
        print()

# Example usage
domain = input("input as :example.com")
result = handler(domain)
print_dns_records(result)
