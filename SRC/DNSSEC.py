import aiohttp
import asyncio
import sys
from colorama import Fore, Style

async def fetch_dns_record(session, domain, dns_type):
    url = f"https://dns.google/resolve?name={domain}&type={dns_type}"
    headers = {'Accept': 'application/dns-json'}

    try:
        async with session.get(url, headers=headers) as response:
            response.raise_for_status()
            dns_response = await response.json()

            return {
                'isFound': bool(dns_response.get('Answer')),
                'answer': dns_response.get('Answer', []),
                'flags': dns_response.get('AD'),
            }
    except Exception as error:
        raise Exception(f"Error fetching {dns_type} record: {error}")

async def handler(domain):
    dns_types = ['DNSKEY', 'DS', 'RRSIG']
    records = {}

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_dns_record(session, domain, dns_type) for dns_type in dns_types]
        results = await asyncio.gather(*tasks)

    for dns_type, result in zip(dns_types, results):
        records[dns_type] = result

    return records

def print_dns_records(records):
    for dns_type, record in records.items():
        print(f"{Fore.RED}{dns_type}{Style.RESET_ALL}")
        print(f"{Fore.RED}{dns_type} - Present? {'✅ Yes' if record['isFound'] else '❌ No'}{Style.RESET_ALL}")
        print()
        print(f"{Fore.GREEN}    Recursion Desired (RD)✅{Style.RESET_ALL}")
        print(f"{Fore.GREEN}    Recursion Available (RA)✅{Style.RESET_ALL}")
        print(f"{Fore.GREEN}    TrunCation (TC)❌{Style.RESET_ALL}")
        print(f"{Fore.GREEN}    Authentic Data (AD) {'✅' if record['flags'] else '❌'}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}    Checking Disabled (CD)❌{Style.RESET_ALL}")
        print()

# Example usage
async def main():
    print ( "====================")
    print(Fore.BLUE + "  DNSSEC " + Style.RESET_ALL)
    print( "====================\n")

    domain = sys.argv[1]
    result = await handler(domain)
    print_dns_records(result)

if __name__ == "__main__":
    asyncio.run(main())
