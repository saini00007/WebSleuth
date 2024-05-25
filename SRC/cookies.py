import aiohttp
import asyncio
import sys

# ANSI escape codes for colorization
GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

async def get_cookie_info(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            cookies = response.cookies

           

            cookie_info = {}
            for key, cookie in cookies.items():
                cookie_info[key] = {
                    "Domain": cookie.get("domain"),
                    "Path": cookie.get("path"),
                    "Expires": cookie.get("expires"),
                    "Secure": cookie.get("secure")
                }
        
            return cookie_info


async def main():
    url = sys.argv[1]
    
    info = await get_cookie_info(url)
    if not info:
                print("\n")
                print("====================")
                print(BLUE + "Cookies " + RESET)
                print("====================\n")
                print(RED +"No cookies found\n" +RESET)
    else:
       for cookie_name, cookie_data in info.items():
        print("====================")
        print(BLUE + "Cookies " + RESET)
        print("====================\n")
        print(f"{GREEN}Cookie Type: {cookie_name}{RESET}")
        for key, value in cookie_data.items():
            if value:
                print(f"{key}: {GREEN}{value}{RESET}")
            else:
                print(f"{key}: {RED}N/A{RESET}")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python filename.py <url>")
        sys.exit(1)
    else:
        asyncio.run(main())
