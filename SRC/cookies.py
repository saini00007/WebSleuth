import aiohttp
import asyncio
import sys

# ANSI escape codes for colorization
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[93m"
RESET = "\033[0m"

async def get_cookie_info(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            cookies = response.cookies

            #cookie_info = {}
            #for cookie in cookies:
             #   print(type(cookie))  # Add this line to check the type of cookie
              #  cookie_info[cookie.name] = {
               #     "Domain": cookie.domain,
                #    "Path": cookie.path,
                 #   "Expires": cookie.expires,
                  #  "Secure": cookie.secure
                #}
            return cookies


async def main():
    url = sys.argv[1]
    
    info = await get_cookie_info(url)
    for cookie_name, cookie_data in info.items():
        print("====================")
        print(BLUE + "Cookies " + RESET)
        print("====================\n")
        print(f"{GREEN}Cookie: {cookie_name}{RESET}")
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
