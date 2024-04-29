import requests
import re

def check_url(url):
    try:
        # Check if the URL includes a protocol
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url
            
            
        # Check if the URL matches the pattern
        if re.match(r'^https?://(?:www\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_+.~#?&/=]*)$', url):
            #return url
            pass
        else:
            raise ValueError("Invalid URL format. Please enter a valid URL.")

        response = requests.get(url)
        if response.status_code == 200:
            return url
        else:
            raise ConnectionError(f"The URL '{url}' is not responding or invalid url. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"The URL '{url}' is invalid or not responding.")

def has_waf(waf):
    return {
        'hasWaf': True,
        'waf': waf,
    }


def check_waf(url):
    full_url = url if url.startswith('http') else f'http://{url}'
    
    try:
        response = requests.get(full_url, timeout=10)
        headers = response.headers

        if 'server' in headers and 'cloudflare' in headers['server'].lower():
            return has_waf('Cloudflare')
        elif 'x-powered-by' in headers and 'AWS Lambda' in headers['x-powered-by']:
            return has_waf('AWS WAF')
        elif 'server' in headers and 'akamaighost' in headers['server'].lower():
            return has_waf('Akamai')
        elif 'server' in headers and 'sucuri' in headers['server'].lower():
            return has_waf('Sucuri')
        elif 'server' in headers and 'barracudawaf' in headers['server'].lower():
            return has_waf('Barracuda WAF')
        elif 'server' in headers and ('f5 big-ip' in headers['server'].lower() or 'big-ip' in headers['server'].lower()):
            return has_waf('F5 BIG-IP')
        elif 'x-sucuri-id' in headers or 'x-sucuri-cache' in headers:
            return has_waf('Sucuri CloudProxy WAF')
        elif 'server' in headers and 'fortiweb' in headers['server'].lower():
            return has_waf('Fortinet FortiWeb WAF')
        elif 'server' in headers and 'imperva' in headers['server'].lower():
            return has_waf('Imperva SecureSphere WAF')
        elif 'x-protected-by' in headers and 'sqreen' in headers['x-protected-by'].lower():
            return has_waf('Sqreen')
        elif 'x-waf-event-info' in headers:
            return has_waf('Reblaze WAF')
        elif 'set-cookie' in headers and '_citrix_ns_id' in headers['set-cookie']:
            return has_waf('Citrix NetScaler')
        elif 'x-denied-reason' in headers or 'x-wzws-requested-method' in headers:
            return has_waf('WangZhanBao WAF')
        elif 'x-webcoment' in headers:
            return has_waf('Webcoment Firewall')
        elif 'server' in headers and 'yundun' in headers['server'].lower():
            return has_waf('Yundun WAF')
        elif 'x-yd-waf-info' in headers or 'x-yd-info' in headers:
            return has_waf('Yundun WAF')
        elif 'server' in headers and 'safe3waf' in headers['server'].lower():
            return has_waf('Safe3 Web Application Firewall')
        elif 'server' in headers and 'naxsi' in headers['server'].lower():
            return has_waf('NAXSI WAF')
        elif 'x-datapower-transactionid' in headers:
            return has_waf('IBM WebSphere DataPower')
        else:
            return {'hasWaf': False}
            
    except requests.exceptions.Timeout:
        return {'hasWaf': False, 'error': 'Request timed out'}
    except requests.exceptions.RequestException as e:
        return {'hasWaf': False, 'error': str(e)}
    except Exception as e:
        return {'statusCode': 500, 'body': {'error': str(e)}}

if __name__ == "__main__":
    text = "\nFirewall (WAB-Web Application Firewall)\n" 
    print(text)
    try:  
        url = input("Enter the URL to check WAF: ")
        valid_url = check_url(url)
        result = check_waf(valid_url)
        if result['hasWaf']:
            print("\n{:<10} {:^} {:>}".format("Firewall", ":" + " " * 5, "YES"))
            print("{:<10} {:^} {:>}".format("WAF", ":" + " " * 5, result['waf']))
        else:
            print("\n{:<10} {:^} {:>}".format("Firewall", ":" + " " * 5,"NO"))
        #print(result)
        if 'error' in result:
            print("Error:", result['error'])
    except Exception as e:
        print("{} {}".format("\nError: ", e))
