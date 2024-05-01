import socket
import requests

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except Exception as e:
        return str(e)

def get_location(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        if response.status_code == 200:
            ip_info = response.json()
            location = ip_info.get('city') + ', ' + ip_info.get('country')
            return location
        else:
            return "Location not available"
    except Exception as e:
        return str(e)

# Example usage
url = input("Enter the URL: ")
ip_address = get_ip_address(url)
if ip_address:
    print("IP Address:", ip_address)
    location = get_location(ip_address)
    print("Location:", location)
else:
    print("Failed to retrieve IP address for the provided URL.")
