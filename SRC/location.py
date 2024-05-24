import aiohttp
import asyncio
from scapy.all import *
from urllib.parse import urlparse
import socket
import sys

async def get_domain_from_url(url):
    parsed_uri = urlparse(url)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    return domain

async def get_ip_location(ip):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://ipapi.co/{ip}/json/") as response:
            data = await response.json()
            return data

def colorize(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    return f"{colors[color]}{text}{colors['reset']}"

def print_location_details(location):
    
    keys = [
        'IP Address', 'City', 'Region', 'Country Code', 'Country', 'Continent Code',
        'Postal Code', 'Latitude', 'Longitude', 'Timezone', 'UTC Offset', 'Country Calling Code',
        'Currency', 'Currency Name', 'Languages', 'ASN', 'Organization', 'Hostname'
    ]
    print("====================")
    print(colorize( "  Server Location ", "blue",))

    print("====================\n")
    print_location_details(location)
    for key in keys:
        value = location.get(key.lower().replace(' ', '_'), 'N/A')
        print(colorize(key + ':', 'red'), colorize(value, 'green'))

async def main():
    url = sys.argv[1]
    domain = await get_domain_from_url(url)
    ip = socket.gethostbyname(domain)
    location = await get_ip_location(ip)
    

if __name__ == "__main__":
    asyncio.run(main())
