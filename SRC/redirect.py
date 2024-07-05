import requests
import sys

def follow_redirects(url):
    try:
        # Initialize an empty list to store redirect URLs
        redirects = []
        
        # Perform a GET request and allow redirects
        response = requests.get(url, allow_redirects=True)
        
        # Append the original URL to the redirects list
        redirects.append(url)
        
        # Collect all the redirects
        for resp in response.history:
            redirects.append(resp.url)
        
        # Append the final URL (where the chain ends)
        redirects.append(response.url)
        
        # Remove duplicates and print the results
        redirects = list(dict.fromkeys(redirects))
        print(f"\033[31mSite {len(redirects) } redirects when contacting host:")
        for redirect in redirects:
            print(f"\033[32m ↳ {redirect}")
        
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    
    
    url = sys.argv[1]
    follow_redirects(url)

if __name__ == "__main__":
    print("\033[0m====================")
    print( "\033[34mSite Redirects \033[0m" )
    print("====================\n")
    main()
    print("\n")
