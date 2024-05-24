import requests
from urllib.parse import urlparse, urljoin
import sys
from colorama import Fore, Style

SECURITY_TXT_PATHS = [
    '/security.txt',
    '/.well-known/security.txt',
]

def parse_result(result):
    output = {}
    counts = {}
    lines = result.split('\n')
    for line in lines:
        if not line.startswith("#") and not line.startswith("-----") and line.strip() != '':
            key_value = line.split(':', 1)
            if len(key_value) == 2:
                key = key_value[0].strip()
                value = key_value[1].strip()
                if key in output:
                    counts[key] = counts.get(key, 0) + 1
                    key += str(counts[key])
                output[key] = value
    return output

def is_pgp_signed(result):
    return '-----BEGIN PGP SIGNED MESSAGE-----' in result

def handler(url_param):
    try:
        url = urlparse(url_param) if '://' in url_param else urlparse('https://' + url_param)
    except Exception as e:
        raise ValueError('Invalid URL or URL is not responding to this query.')

    base_url = url._replace(path='').geturl()

    for path in SECURITY_TXT_PATHS:
        try:
            result = fetch_security_txt(base_url, path)
            if result and '<html' in result:
                return {'isPresent': False}
            if result:
                return {
                    'isPresent': True,
                    'foundIn': path,
                    'content': result,
                    'isPgpSigned': is_pgp_signed(result),
                    'fields': parse_result(result),
                }
        except Exception as e:
            raise Exception(str(e))

    return {'isPresent': False}

def fetch_security_txt(base_url, path):
    url = urljoin(base_url, path)
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

if __name__ == "__main__":
    print("====================\n")
    print(Fore.BLUE + "  Security Text \n" + Style.RESET_ALL)
    print("====================\n")
    
    try:
        url = sys.argv[1]
        result = handler(url)
        if result['isPresent']:
            print("====================\n")
            print(Fore.BLUE + "  Security Text \n" + Style.RESET_ALL)
            print("====================\n")
    
            print("\n{:<20} {:^} {:<10}".format(Fore.GREEN + "Security.txt", "-->" + " " * 5, "present"))
            print(Style.RESET_ALL)
            print("{:<20} {:^} {:<10}".format("File Location", ":" + " " * 5, result['foundIn']))
            print("{:<20} {:^} {:<10}".format("PGP Signed", ":" + " " * 5, "Yes" if result['isPgpSigned'] else "No"))
            for key, value in result['fields'].items():
              print("{:<20} {:^} ".format(Fore.RED + key, ":" + " " * 5), end="")
              print(Fore.GREEN + "{}".format(value))
              print(Style.RESET_ALL)
        else:
            print("\n{:<20} {:^} ".format(Fore.RED + "Security.txt", "-->" + " " * 5 + "not present")) 
            print(Style.RESET_ALL)

    except Exception as e:
        print("{} {}".format("\nError: ", e))
