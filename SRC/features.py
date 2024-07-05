import requests
import re
import sys

def check_feature(url, feature):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            if re.search(feature + r'[^a-zA-Z0-9_-]', html_content, re.IGNORECASE):
                return 'Live'
            else:
                return 'Dead'
        else:
            return 'Error: Unable to fetch URL'
    except Exception as e:
        return 'Error: {}'.format(str(e))

def main():
    url = sys.argv[1]

    features = {
        'ssl': 'ssl',
        'javascript': 'javascript-library1|javascript',
        'framework': 'framework1',
        'us-hosting': 'us-hosting3',
        'cloud-hosting': 'cloud-hosting2',
        'cloud-paas': 'cloud-paas3',
        'server-location': 'server-location1',
        'application-performance': 'application-performance1',
        'audience-measurement': 'audience-measurement2',
        'dmarc': 'dmarc1'
    }

    
    for key, value in features.items():
        result = check_feature(url, value)
        print(f"\033[31m{key} :\033[32m {result}")

if __name__ == "__main__":
    print("====================")
    print( "\033[34mSite Features \033[0m" )
    print("====================\n")
    main()
    print("\n")