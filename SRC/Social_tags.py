import requests
from bs4 import BeautifulSoup
import re
import sys
from colorama import Fore, Style, init


init()
def get_metadata(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        metadata = {
            # Basic meta tags
            'title': soup.find('title').get_text() if soup.find('title') else None,
            'description': soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else None,
            'keywords': soup.find('meta', attrs={'name': 'keywords'})['content'] if soup.find('meta', attrs={'name': 'keywords'}) else None,
            'canonicalUrl': soup.find('link', attrs={'rel': 'canonical'})['href'] if soup.find('link', attrs={'rel': 'canonical'}) else None,

            # OpenGraph Protocol
            'ogTitle': soup.find('meta', attrs={'property': 'og:title'})['content'] if soup.find('meta', attrs={'property': 'og:title'}) else None,
            'ogType': soup.find('meta', attrs={'property': 'og:type'})['content'] if soup.find('meta', attrs={'property': 'og:type'}) else None,
            'ogImage': soup.find('meta', attrs={'property': 'og:image'})['content'] if soup.find('meta', attrs={'property': 'og:image'}) else None,
            'ogUrl': soup.find('meta', attrs={'property': 'og:url'})['content'] if soup.find('meta', attrs={'property': 'og:url'}) else None,
            'ogDescription': soup.find('meta', attrs={'property': 'og:description'})['content'] if soup.find('meta', attrs={'property': 'og:description'}) else None,
            'ogSiteName': soup.find('meta', attrs={'property': 'og:site_name'})['content'] if soup.find('meta', attrs={'property': 'og:site_name'}) else None,

            # Twitter Cards
            'twitterCard': soup.find('meta', attrs={'name': 'twitter:card'})['content'] if soup.find('meta', attrs={'name': 'twitter:card'}) else None,
            'twitterSite': soup.find('meta', attrs={'name': 'twitter:site'})['content'] if soup.find('meta', attrs={'name': 'twitter:site'}) else None,
            'twitterCreator': soup.find('meta', attrs={'name': 'twitter:creator'})['content'] if soup.find('meta', attrs={'name': 'twitter:creator'}) else None,
            'twitterTitle': soup.find('meta', attrs={'name': 'twitter:title'})['content'] if soup.find('meta', attrs={'name': 'twitter:title'}) else None,
            'twitterDescription': soup.find('meta', attrs={'name': 'twitter:description'})['content'] if soup.find('meta', attrs={'name': 'twitter:description'}) else None,
            'twitterImage': soup.find('meta', attrs={'name': 'twitter:image'})['content'] if soup.find('meta', attrs={'name': 'twitter:image'}) else None,

            # Misc
            'themeColor': soup.find('meta', attrs={'name': 'theme-color'})['content'] if soup.find('meta', attrs={'name': 'theme-color'}) else None,
            'robots': soup.find('meta', attrs={'name': 'robots'})['content'] if soup.find('meta', attrs={'name': 'robots'}) else None,
            'googlebot': soup.find('meta', attrs={'name': 'googlebot'})['content'] if soup.find('meta', attrs={'name': 'googlebot'}) else None,
            'generator': soup.find('meta', attrs={'name': 'generator'})['content'] if soup.find('meta', attrs={'name': 'generator'}) else None,
            'viewport': soup.find('meta', attrs={'name': 'viewport'})['content'] if soup.find('meta', attrs={'name': 'viewport'}) else None,
            'author': soup.find('meta', attrs={'name': 'author'})['content'] if soup.find('meta', attrs={'name': 'author'}) else None,
            'publisher': soup.find('link', attrs={'rel': 'publisher'})['href'] if soup.find('link', attrs={'rel': 'publisher'}) else None,
            'favicon': soup.find('link', attrs={'rel': 'icon'})['href'] if soup.find('link', attrs={'rel': 'icon'}) else None
        }

        return metadata

    except requests.exceptions.RequestException as e:
        raise Exception('Failed fetching metadata:', str(e))
    except (KeyError, AttributeError) as e:
        raise Exception('Error parsing metadata:', str(e))


def print_colored_metadata(metadata):
    print ( "====================\n")
    print(Fore.BLUE + "  Social Tags \n" + Style.RESET_ALL)
    print( "====================\n")
    theme_color = metadata.get('themeColor', 'N/A')
    if theme_color != 'N/A' and theme_color is not None:
        # Convert the hex color code to its corresponding ANSI color code
        theme_color_ansi = "\033[48;2;{};{};{}m".format(*tuple(int(theme_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)))
        # Reset color after printing
        reset_color = "\033[0m"
    else:
        theme_color_ansi = ''
        reset_color = ''

    print("\n{:<15} {:^10} {:<15}".format("Title", ":", str(metadata.get('title', 'N/A'))))

    print("{:<15} {:^10} {:<15}".format("Description", ":", str(metadata.get('description', 'N/A'))))

    print("{:<15} {:^10} {:<15}".format("Keywords", ":", str(metadata.get('keywords', 'N/A'))))

    print("{:<15} {:^10} {:<15}".format("Canonical URL", ":", str(metadata.get('canonicalUrl', 'N/A'))))

    print("{:<15} {:^10} {:<15}".format("Theme Color", ":", theme_color_ansi + str(theme_color) + reset_color))

    print("{:<15} {:^10} {:<15}".format("Twitter Site", ":", str(metadata.get('twitterSite', 'N/A'))))


if __name__ == "__main__":
    

    try:
        url = sys.argv[1]
        
        metadata = get_metadata(url)
        print_colored_metadata(metadata)
    except Exception as e:
        print("{} {}".format("\nError: ", e))
