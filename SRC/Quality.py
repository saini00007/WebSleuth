import json
import subprocess
from colorama import Fore, Style
import sys


def run_lighthouse(url):
   
    try:
        # Run Lighthouse command with headless Chrome
        
        subprocess.run("exit", shell=True)
        cmd = f" lighthouse {url} --quiet --output=json --chrome-flags='--headless --disable-gpu'"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error running Lighthouse:", e)
        return None

def print_quality_metrics(url):
    
    lighthouse_data = run_lighthouse(url)
    if lighthouse_data:
        
        for category_name, category_data in lighthouse_data['categories'].items():
            category_score = int(category_data['score'] * 100)
            print(f"\n{Fore.YELLOW + '----- ' + Fore.RED + Style.BRIGHT + category_name.capitalize() + Fore.GREEN +   ' : '  + str(category_score) + '%' + Style.RESET_ALL}\n")
            if 'auditRefs' in category_data:
                for audit_ref in category_data['auditRefs']:
                    audit_name = audit_ref['id']
                    audit_result = lighthouse_data['audits'][audit_name]
                    status = Fore.GREEN + "✅ " + Style.RESET_ALL if audit_result['score'] == 1 else Fore.RED + "❌ " + Style.RESET_ALL
                    display_value = f"{'-Value : ' + Fore.GREEN + audit_result['displayValue']}\n" if 'displayValue' in audit_result else ""
                    print(f"{Fore.RED +'-> '+ audit_result['title'] + ' : ' + Style.RESET_ALL}{status}\n")
                    print(display_value)
    else:
        print("Failed to fetch quality metrics.")

if __name__ == "__main__":
    
    
    url = sys.argv[1]
    
   
    
    print("\033[0m====================")
    print( "\033[34mQuality of Services  \033[0m" )
    print("====================\n")
    print_quality_metrics(url)
