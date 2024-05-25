import aiohttp
import asyncio
import socket
import sys
from colorama import Fore, Style
from urllib.parse import urlparse

async def resolve_dns(url, session):
    try:
        # Extract domain from URL
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        
        # Resolve IPv4 addresses
        addresses = socket.gethostbyname_ex(domain)[-1]
        
        results = []
        for address in addresses:
            # Reverse DNS lookup
            try:
                hostname = socket.gethostbyaddr(address)[0]
            except socket.herror:
                hostname = None
            
            # Check if DoH is supported directly
            try:
                async with session.get(f'https://{address}/dns-query') as response:
                    doh_direct_supports = response.status == 200
            except aiohttp.ClientError:
                doh_direct_supports = False
            
            results.append({
                'address': address,
                'hostname': hostname,
                'dohDirectSupports': doh_direct_supports
            })

        return {
            'domain': domain,
            'dns': results
        }
    except Exception as e:
        raise Exception(f"An error occurred while resolving DNS. {str(e)}")

async def print_result(result):
    try:
        print("====================")
        print(Fore.BLUE + "  DNS Servers " + Style.RESET_ALL)
        print("====================\n")
 
        n = 1
        for item in result["dns"]:
            print(Fore.BLUE + f"DNS Server No.{n}" + Style.RESET_ALL)

            if "address" in item:
                print("{:<20} {:^} {:>10}".format(Fore.RED + "IP Address" + Style.RESET_ALL, ":" + " " * 5, Fore.GREEN + str(item["address"]) + Style.RESET_ALL))
            if "hostname" in item:
                print("{:<20} {:^} {:>10}".format(Fore.RED + "Hostname" + Style.RESET_ALL, ":" + " " * 5, Fore.GREEN + str(item["hostname"]) + Style.RESET_ALL))
            if "dohDirectSupports" in item:
                print("{:<20} {:^} {:>10}".format(Fore.RED + "DoH Support" + Style.RESET_ALL, ":" + " " * 5, Fore.GREEN + str(item["dohDirectSupports"]) + Style.RESET_ALL))

            print("\n")
            n = n + 1
    except Exception as e:
        raise Exception(f"An error occurred while printing result: {str(e)}")

async def main():
    async with aiohttp.ClientSession() as session:
        url = sys.argv[1]
        if not url.startswith('https://'):
            print("Please provide a URL starting with 'https://'")
            return
        
        resolved_dns = await resolve_dns(url, session)
        await print_result(resolved_dns)
        


if __name__ == "__main__":
    asyncio.run(main())
