import requests
from colorama import Fore, Style

def get_headers(url):
    try:
        response = requests.head(url)
        headers = response.headers
        return headers
    except Exception as e:
        return str(e)

def print_colored_headers(headers):
    if headers:
        for key, value in headers.items():
            print(Fore.RED + key + ":" + Style.RESET_ALL + Fore.GREEN + value + Style.RESET_ALL)
    else:
        print("Failed to retrieve headers for the provided URL.")

# Example usage
url = input("Enter the URL: ")
headers = get_headers(url)
print_colored_headers(headers)
