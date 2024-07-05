import aiohttp
import asyncio
import sys

async def check_server_status(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.head(url) as response:
                if response.status == 200:
                    print("\033[31mServer Status: ✅ \033[32mOnline\033[0m")
                else:
                    print("\033[31mServer Status: ❌ Offline\033[0m")
                print("\033[31mStatus Code: \033[0m\033[32m", response.status, "\033[0m")
                print("\033[31mResponse Time: \033[0m\033[32m", response.headers.get('Server-Timing'), "\033[0m")
    except aiohttp.ClientError as e:
        print("\033[31mError connecting to the server\033[0m", )

if __name__ == "__main__":
    print("\033[0m====================")
    print( "\033[34mServer Status \033[0m" )
    print("====================\n")
    url = sys.argv[1]
    asyncio.run(check_server_status(url))
    print("\n")
