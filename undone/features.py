import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def extract_site_features(url):
    try:
        # Parse the URL
        parsed_url = urlparse(url)

        # If the URL lacks a scheme (e.g., http:// or https://), add https:// by default
        if not parsed_url.scheme:
            url = "https://" + url

        # Fetch the HTML content of the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract site features
        features = {}
        current_category = None
        for li in soup.find_all('li'):
            text = li.get_text().strip()
            if text.endswith(':'):
                current_category = text[:-1]
            else:
                feature, status = text.rsplit(' ', 1)
                features.setdefault(current_category, []).append((feature, status))

        # Print site features in the specified format
        print("Site Features:")
        for category, features_list in features.items():
            print(category)
            for feature, status in features_list:
                print(f"{feature} {status}")

    except requests.RequestException as e:
        print("Error fetching URL:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

# Example usage
url = input("Enter a URL: ")
extract_site_features(url)
