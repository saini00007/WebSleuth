import requests
from urllib.parse import urlparse
import sys

def colorize(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    return f"{colors[color]}{text}{colors['reset']}"

def check_headers(url, headers_to_check):
    try:
        response = requests.get(url)
        response_headers = response.headers
        
        for header in headers_to_check:
            if header in response_headers:
                print(colorize("[+]", 'red'), colorize(f"{header:<30}: ", 'red'), colorize("YES", 'green'))
            else:
                print(colorize("[-]", 'red'), colorize(f"{header:<30}: ", 'red'), colorize("NO", 'green'))

    except requests.exceptions.RequestException as e:
        print(colorize(f"Error occurred during the request: {e}", 'red'))

if __name__ == "__main__":
    print("====================")
    print(colorize( "  HTTP Security", "blue",))

    print("====================\n")
    headers_to_check = ["strict-transport-security", "x-frame-options", "x-content-type-options","x-xss-protection", "content-security-policy"]
    try:
        url = sys.argv[1]
        
        check_headers(url, headers_to_check)
    except Exception as e:
        print(colorize("\nError:", 'red'), e)
    print("\n")   
