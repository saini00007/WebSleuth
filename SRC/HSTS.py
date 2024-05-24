import aiohttp
import sys
import asyncio
import re

def colorize(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[93m",
        "reset": "\033[0m"
    }
    return f"{colors[color]}{text}{colors['reset']}"

async def check_hsts_and_print_result(url):
    result = await check_hsts_compatibility(url)
    await print_colored_result(result)

async def check_hsts_compatibility(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.head(url) as response:
                headers = response.headers
                hsts_header = headers.get('strict-transport-security')

                if not hsts_header:
                    return {'message': 'HSTS not Enabled. \nSite does not serve any HSTS headers.', 'compatible': False, 'hstsHeader': None}

                max_age_match = re.search(r'max-age=(\d+)', hsts_header)
                includes_subdomains = 'includeSubDomains' in hsts_header
                preload = 'preload' in hsts_header

                details = {
                    'HSTS Enabled': True,
                    'max-age': max_age_match.group(1) if max_age_match else 'N/A',
                    'includeSubDomains': includes_subdomains,
                    'preload': preload
                }

                if max_age_match and int(max_age_match.group(1)) >= 10886400 and includes_subdomains and preload:
                    return {'message': 'Site is compatible with the HSTS preload list!', 'compatible': True, 'hstsHeader': hsts_header, 'details': details}
                else:
                    return {'message': 'HSTS header does not include all subdomains.', 'compatible': False, 'hstsHeader': hsts_header, 'details': details}

    except Exception as e:
        return {'message': f'Error making request: {str(e)}', 'compatible': False, 'hstsHeader': None}

async def print_colored_result(result):
    print("====================")
    print(colorize( "  HTTP Security", "blue",))

    print("====================\n")
    if result['compatible']:
        print(colorize("\nCompatible : ", 'green'), colorize(result['message'], 'green'))
    else:
        print(colorize("\nIncompatible : ", 'red'), colorize(result['message'], 'red'))

    details = result.get('details')
    if details:
        print(colorize("\nDetails : ", 'green'))
        for key, value in details.items():
            print(colorize(f"  - {key:<20}", 'green'), colorize(":", 'green'), colorize(str(value), 'green'))
                
if __name__ == "__main__":
   

    url = sys.argv[1]
    # Run the coroutine and handle exceptions within asyncio.run()
    asyncio.run(check_hsts_and_print_result(url))
