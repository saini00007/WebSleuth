import subprocess
import sys
import tldextract

def extract_domain_name(url):
    extracted = tldextract.extract(url)
    domain_name = f"{extracted.domain}.{extracted.suffix}"
    print(domain_name)
    
    return domain_name

# Example usage


def get_txt_records(domain):
    try:
        # Execute dig command to query TXT records for the domain
        result = subprocess.run(['dig', 'TXT', domain], capture_output=True, text=True)
       
        
        # Extract TXT record data from the result
        txt_records = {}
        for line in result.stdout.split('\n'):
            if 'TXT' in line:
                parts = line.strip().split('"')
                if len(parts) >= 3:
                    key = parts[1].split('=')[0].strip()
                    value = parts[1].split('=')[1].strip()
                    txt_records[key] = value
        
        return txt_records
    except Exception as e:
        return {}

def main():
    url = sys.argv[1]
    domain = extract_domain_name(url)
    print("\033[0m====================")
    print( "\033[34mTXT Records \033[0m" )
    print("====================\n")
    txt_records = get_txt_records(domain)
    if txt_records:
        for key, value in txt_records.items():
            print(f"\033[31m{key} = \033[32m{value}")
    else:
        print("\033[31mNo TXT records found.")

if __name__ == "__main__":
    main()
