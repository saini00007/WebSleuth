import requests
import base64
import tldextract
import sys

# Replace with your VirusTotal API key
VT_API_KEY = '57e3de8428a9e14885e553719f4800e738d2150b1058e51ee9b1dc0b9b0a044d'

def url_to_base64(url):
    """Encode URL to a format suitable for VirusTotal API."""
    return base64.urlsafe_b64encode(url.encode()).decode().strip("=")

def extract_domain(url):
    """Extract domain from URL using tldextract."""
    extracted = tldextract.extract(url)
    return f"{extracted.domain}.{extracted.suffix}"

def check_virus_total(url):
    """Check URL against VirusTotal and return status."""
    headers = {
        'x-apikey': VT_API_KEY
    }
    encoded_url = url_to_base64(url)
    analysis_url = f"https://www.virustotal.com/api/v3/urls/{encoded_url}"
    
    try:
        response = requests.get(analysis_url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError if the response was an HTTP error
        analysis_data = response.json()
        
        if 'data' in analysis_data:
            positives = analysis_data['data']['attributes']['last_analysis_stats']['malicious']
            if positives > 0:
                return False, analysis_data
            return True, analysis_data
        else:
            print("Unexpected response structure:", analysis_data)
            return False, analysis_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return False, {}
    except Exception as err:
        print(f"Other error occurred: {err}")
        return False, {}




def get_security_status(url):
    """Get overall security status of the URL."""
    vt_safe, vt_details = check_virus_total(url)
    
    return {
        "\033[34mAccording to VirusTotal report Site is ": "\033[32m✅ Safe" if vt_safe else f"\033[31m❌ Not Safe",
       }

if __name__ == "__main__":
    print("====================")
    print( "\033[34mSite Scan \033[0m" )
    print("====================\n")
    url = sys.argv[1]  # Replace with the target URL
    domain = extract_domain(url)
    status = get_security_status(domain)
    for key, value in status.items():
        print(f"{key}: {value}")
    print("\n")