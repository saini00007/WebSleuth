import requests
from colorama import Fore, Style

def get_html_size(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        size_in_bytes = len(html_content.encode('utf-8'))
        return size_in_bytes
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error fetching HTML size: {e}")

def get_carbon_data(size_in_bytes):
    try:
        api_url = f"https://api.websitecarbon.com/data?bytes={size_in_bytes}&green=0"
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error fetching carbon data: {e}")

def handler(url):
    try:
        size_in_bytes = get_html_size(url)
        carbon_data = get_carbon_data(size_in_bytes)
        
        if 'statistics' not in carbon_data or (carbon_data['statistics']['adjustedBytes'] == 0 and carbon_data['statistics']['energy'] == 0):
            return {"skipped": "Not enough info to get carbon data"}
        
        carbon_data['scanUrl'] = url
        return carbon_data
    except Exception as e:
        raise ValueError(f"Error: {e}")

# Example usage:
url = "https://google.com/"
result = handler(url)

def print_carbon_data(data):
    print(Fore.GREEN + "Carbon Footprint")
    print(Fore.RED + f"{Style.BRIGHT}HTML Initial Size:{Fore.YELLOW} {data['statistics']['adjustedBytes']} bytes")
    print(Fore.RED + f"{Style.BRIGHT}CO2 for Initial Load:{Fore.YELLOW} {data['statistics']['co2']['grid']['grams']} grams")
    print(Fore.RED + f"{Style.BRIGHT}Energy Usage for Load:{Fore.YELLOW} {data['statistics']['energy']:.4f} KWg")
    print(Fore.RED + f"{Style.BRIGHT}CO2 Emitted:{Fore.YELLOW} {data['statistics']['co2']['renewable']['grams']} grams")

print_carbon_data(result)
