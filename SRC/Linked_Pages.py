import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import sys

def handler(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        internal_links_map = {}
        external_links_map = {}

        # Get all links on the page
        for link in soup.find_all('a', href=True):
            href = link['href']
            absolute_url = urljoin(url, href)
            
            # Check if absolute / relative, append to appropriate map or increment occurrence count
            if absolute_url.startswith(url):
                internal_links_map[absolute_url] = internal_links_map.get(absolute_url, 0) + 1
            elif href.startswith(('http://', 'https://')):
                external_links_map[absolute_url] = external_links_map.get(absolute_url, 0) + 1

        # Sort by most occurrences, remove duplicates, and convert to list
        internal_links = sorted(internal_links_map.keys(), key=lambda k: internal_links_map[k], reverse=True)
        external_links = sorted(external_links_map.keys(), key=lambda k: external_links_map[k], reverse=True)

        # If there were no links, then return a message
        if not internal_links and not external_links:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'skipped': 'No internal or external links found. This may be due to the website being dynamically rendered, '
                               'using a client-side framework (like React), and without SSR enabled. '
                               'That would mean that the static HTML returned from the HTTP request doesn\'t contain any meaningful content for analysis. '
                               'You can rectify this by using a headless browser to render the page instead.'
                })
            }

        # Extract only the part of the internal links that comes after the provided URL
        base_url_len = len(url)
        internal_links = [link[base_url_len:] if link.startswith(url) else link for link in internal_links]

        return {'internal': internal_links, 'external': external_links}

    except Exception as e:
        raise Exception(str(e))

def colorize(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    return f"{colors[color]}{text}{colors['reset']}"

def main():
    
    try:
        url = sys.argv[1]
        print("====================")
        print(colorize( "  Linked Pages ", "blue",))

        print("====================\n")
        result = handler(url)
        if 'internal' not in result:
            print(colorize("Error:", 'red'), result['body'])
        else:
            
            print(colorize("\nTotal internal links found:", 'red'), colorize(len(result['internal']), 'green'))
            print(colorize("\nInternal Links:", 'red'))
            for link in result['internal']:
                print(colorize(link, 'green'))
    except Exception as e:
        print(colorize("Error:", 'red'), e)

if __name__ == "__main__":
    main()
