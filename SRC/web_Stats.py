import aiohttp
import asyncio
import sys
import tldextract
from datetime import datetime

def extract_domain(url):
    extracted = tldextract.extract(url)
    return extracted.domain + '.' + extracted.suffix

API_BASE_URL = "https://tranco-list.eu/api/"

def remove_http_www(url):
    if url.startswith("http://www."):
        return url[len("http://www."):]
    elif url.startswith("https://www."):
        return url[len("https://www."):]
    return url

async def get_global_rank(url):
    try:
        async with aiohttp.ClientSession() as session:
            endpoint = f"{API_BASE_URL}/ranks/domain/{url}"
            async with session.get(endpoint) as response:
                if response.status == 200:
                    data = await response.json()
                    ranks = data.get("ranks", [])
                    
                    if ranks:
                        # Find the latest date in the ranks data
                        latest_rank = max(ranks, key=lambda x: x["date"])
                        latest_date = latest_rank["date"]
                        latest_rank_value = latest_rank["rank"]
                        
                        print(f"\033[31mThe global rank of {url} on {latest_date} is: \033[32m{latest_rank_value}\n")
                    else:
                        print("\033[31mNo rank data found for the given domain.\n")
                else:
                    print("\033[31mNo rank found for the given domain.\n")
    except Exception as e:
        print("\033[31mAn error occurred:\n", e)

async def main():
    print("\033[0m====================")
    print( "\033[34mGlobal Rank \033[0m" )
    print("====================\n")
    url = sys.argv[1]
    domain = extract_domain(url)
    await get_global_rank(domain)

if __name__ == "__main__":
    asyncio.run(main())
