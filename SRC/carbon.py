import aiohttp
import asyncio
from colorama import Fore, Style
import sys

async def get_html_size(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                html_content = await response.text()
                size_in_bytes = len(html_content.encode('utf-8'))
                return size_in_bytes
    except aiohttp.ClientError as e:
        raise ValueError(f"Error fetching HTML size: {e}")

async def get_carbon_data(size_in_bytes):
    try:
        api_url = f"https://api.websitecarbon.com/data?bytes={size_in_bytes}&green=0"
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                response.raise_for_status()
                return await response.json()
    except aiohttp.ClientError as e:
        raise ValueError(f"Error fetching carbon data: {e}")

async def handler(url):
    try:
        size_in_bytes = await get_html_size(url)
        carbon_data = await get_carbon_data(size_in_bytes)
        
        if 'statistics' not in carbon_data or (carbon_data['statistics']['adjustedBytes'] == 0 and carbon_data['statistics']['energy'] == 0):
            return {"skipped": "Not enough info to get carbon data"}
        
        carbon_data['scanUrl'] = url
        return carbon_data
    except Exception as e:
        raise ValueError(f"Error: {e}")

async def print_carbon_data(data):
    
    print(Fore.RED + f"{Style.BRIGHT}HTML Initial Size:{Fore.GREEN} {data['statistics']['adjustedBytes']} bytes")
    print(Fore.RED + f"{Style.BRIGHT}CO2 for Initial Load:{Fore.GREEN} {data['statistics']['co2']['grid']['grams']} grams")
    print(Fore.RED + f"{Style.BRIGHT}Energy Usage for Load:{Fore.GREEN} {data['statistics']['energy']:.4f} KWg")
    print(Fore.RED + f"{Style.BRIGHT}CO2 Emitted:{Fore.GREEN} {data['statistics']['co2']['renewable']['grams']} grams")

async def main():
    print("====================")
    print(Fore.BLUE + "  Carbon Footprint  " + Style.RESET_ALL)
    print("====================\n")
    url = sys.argv[1]
    result = await handler(url)
    await print_carbon_data(result)

if __name__ == "__main__":
    asyncio.run(main())
