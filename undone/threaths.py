
import requests

# ANSI escape codes for text formatting
ANSI_GREEN = "\033[92m"
ANSI_RED = "\033[91m"
ANSI_BOLD = "\033[1m"
ANSI_RESET = "\033[0m"

def check_threats(url, api_key):
    try:
        # API endpoint for Google Safe Browsing API
        api_url = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

        # Payload for the API request
        payload = {
            "client": {"clientId": "YourCompany", "clientVersion": "1.0"},
            "threatInfo": {
                "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "POTENTIALLY_HARMFUL_APPLICATION", "THREAT_TYPE_UNSPECIFIED"],
                "platformTypes": ["ANY_PLATFORM"],
                "threatEntryTypes": ["URL"],
                "threatEntries": [{"url": url}],
            },
        }

        # Make the API request
        response = requests.post(api_url + "?key=" + api_key, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Check the response
        if response.status_code == 200:
            threat_data = response.json()
            if "matches" in threat_data:
                print(ANSI_BOLD + "Threats" + ANSI_RESET)
                for match in threat_data["matches"]:
                    threat_type = match["threatType"]
                    print(threat_type, end="")
                    if threat_type == "MALWARE":
                        print(ANSI_RED + "❌ Found" + ANSI_RESET)
                    else:
                        print(ANSI_GREEN + "✅ No Threat Found" + ANSI_RESET)
                return
    except requests.RequestException as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

    print("Unable to check threats.")

# Example usage
url = input("Enter a URL: ")
api_key = "AIzaSyAO_p6i_jJlRYKI6q8FIGobaJjqUQLAoZ8"
check_threats(url, api_key)
