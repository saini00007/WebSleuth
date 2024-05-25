import aiohttp
from urllib.parse import urljoin
import asyncio
import sys

# ANSI escape codes for text formatting
ANSI_RED = "\033[31m"
ANSI_GREEN = "\033[32m"
ANSI_BLUE = "\033[34m"
ANSI_BOLD = "\033[1m"
ANSI_RESET = "\033[0m"

async def get_robots_txt(url, session):
    # Get the base URL
    base_url = urljoin(url, "/")

    # Fetch the robots.txt file
    robots_url = urljoin(base_url, "robots.txt")
    async with session.get(robots_url) as response:
        if response.status != 200:
            print("Failed to fetch robots.txt:", response.status)
            return

        # Parse robots.txt and extract rules
        lines = (await response.text()).splitlines()
        user_agent = ""
        crawl_rules = []
        for line in lines:
            if line.lower().startswith("user-agent:"):
                user_agent = line.split(":")[1].strip()
            elif line.lower().startswith(("allow:", "disallow:")):
                rule = line.split(":")[1].strip()
                crawl_rules.append((user_agent, rule))

        # Print crawl rules with style and colors
        print("====================")
        print(ANSI_BLUE + "Crawl Rules " + ANSI_RESET)
        print("====================\n")
        for user_agent, rule in crawl_rules:
            
            print(ANSI_RED+ "User-Agent:", user_agent + ANSI_RESET)
            if "allow" in rule:
                print(ANSI_GREEN + "Allow:", rule + ANSI_RESET)
            else:
                print(ANSI_GREEN + "Disallow:", rule + ANSI_RESET)
            print()

async def main():
    async with aiohttp.ClientSession() as session:
        url = sys.argv[1]
        await get_robots_txt(url, session)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python filename.py <url>")
        sys.exit(1)
    else:
        asyncio.run(main())
