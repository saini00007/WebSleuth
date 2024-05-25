import requests
import sys
from colorama import Fore, Style

def get_http_headers(url):
    
    try:
        response = requests.head(url, allow_redirects=True)
        response.raise_for_status()
        return response.headers
    except requests.RequestException as e:
        #print(f"Error accessing the webpage: {e}")
        return None

def identify_web_technologies(http_headers):
    if not http_headers:
        return None

    technologies = {
        'Server': http_headers.get('Server', 'Unknown'),
        'X-Powered-By': http_headers.get('X-Powered-By', 'Not specified'),
        'X-AspNet-Version': http_headers.get('X-AspNet-Version', 'Not specified'),
    }

    return technologies

if __name__ == "__main__":
    url = sys.argv[1] 

    http_headers = get_http_headers(url)
    if http_headers:
        web_technologies = identify_web_technologies(http_headers)
        print("====================")
        print(Fore.BLUE + "  Web Technologies  " + Style.RESET_ALL)
        print("====================\n")
        for key, value in web_technologies.items():
            print(Fore.RED + f"{key}:" + Fore.GREEN + f" {value}" + Style.RESET_ALL)
              
    else:
        print("====================")
        print(Fore.BLUE + "  Web Technologies  " + Style.RESET_ALL)
        print("====================\n")
        print("Unable to retrieve HTTP headers.")
print("\n")  
