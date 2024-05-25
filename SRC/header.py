import aiohttp
import asyncio
import sys
from colorama import Fore, Style

async def get_headers(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.head(url) as response:
                headers = response.headers
                return headers
    except Exception as e:
        return str(e)

def print_colored_headers(headers):
    print ( "====================")
    print(Fore.BLUE + "  Headers " + Style.RESET_ALL)
    print( "====================\n")
    if headers:
        for key, value in headers.items():
            print(Fore.RED + key + ":" + Style.RESET_ALL + Fore.GREEN + value + Style.RESET_ALL)
    else:
        print("Failed to retrieve headers for the provided URL.")
    print("\n")
# Example usage
async def main():

    url = sys.argv[1]
    headers = await get_headers(url)
    print_colored_headers(headers)

if __name__ == "__main__":
    asyncio.run(main())
