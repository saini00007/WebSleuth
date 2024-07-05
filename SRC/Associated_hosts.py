import aiohttp
import asyncio
from bs4 import BeautifulSoup
import sys
import tldextract

def extract_domain_name(url):
    extracted = tldextract.extract(url)
    domain_name = f"{extracted.domain}.{extracted.suffix}"
    return domain_name

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def get_subdomains(domain):
    subdomains = set()
    url = f"https://crt.sh/?dnsname={domain}&exclude=expired&group=none"
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        soup = BeautifulSoup(html, 'html.parser')
        # Extract subdomains from the table in the HTML
        for row in soup.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) > 4:
                subdomain = cells[4].get_text().strip()
                if subdomain.endswith(domain):
                    subdomains.add(subdomain)
    return subdomains

async def main(domain):
    subdomains = await get_subdomains(domain)
    if subdomains:
        print(f"\033[31mFound {len(subdomains)} subdomains \n")
        for subdomain in sorted(subdomains):
            print("\033[32m",subdomain)
    else:
        print(f"No subdomains found for {domain}.")

if __name__ == "__main__":
    print("\033[0m====================")
    print( "\033[34mSubdomains \033[0m" )
    print("====================\n")
    url = sys.argv[1]
    domain = extract_domain_name(url)
    
    asyncio.run(main(domain))
    print("\n")
