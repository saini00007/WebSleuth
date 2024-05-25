import requests
import sys
from colorama import Fore, Style

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

def print_colored_result(result):
    print ( "====================")
    print(Fore.BLUE + "  Firewall " + Style.RESET_ALL)
    print( "====================")
    if result['hasWaf']:
        print(f"\n{Fore.RED}Firewall{Style.RESET_ALL} : {Fore.GREEN}YES{Style.RESET_ALL}")
        print(f"{Fore.RED}WAF{Style.RESET_ALL}      : {Fore.GREEN}{result['waf']}{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}Firewall{Style.RESET_ALL} : {Fore.GREEN}NO{Style.RESET_ALL}")
    if 'error' in result:
        print(f"Error: {result['error']}")

if __name__ == "__main__":
   

    try:  
        url = sys.argv[1]
        result = check_waf(url)
        print_colored_result(result)
    except Exception as e:
        print(f"{Fore.RED}\nError:{Style.RESET_ALL} {e}")
print("\n")
