import subprocess
import sys
import tldextract

def extract_domain_name(url):
    extracted = tldextract.extract(url)
    domain_name = f"{extracted.domain}.{extracted.suffix}"
    return domain_name



def get_record(domain, record_type):
    try:
        record = subprocess.check_output(['dig', '+short', record_type, domain])
        return record.decode('utf-8').strip()
    except subprocess.CalledProcessError:
        return "Record not found."

if __name__ == "__main__":
    print("\033[0m====================")
    print( "\033[34mEmail Configurations \033[0m" )
    print("====================\n")
    url = sys.argv[1]
    domain = extract_domain_name(url)

    spf_record = get_record(domain, 'TXT')
    print("\033[34mSPF Record:\n\033[0m")
    if spf_record != "Record not found.":
        print("  \033[31mStatus: \033[0m\033[32mFound\033[0m")
        print("  \033[31mContent: \033[0m\033[32m", spf_record, "\033[0m", sep='')
    else:
        print("  \033[31mStatus: \033[0m\033[33mNot found\033[0m")

    dkim_record = get_record(f'_domainkey.{domain}', 'TXT')
    print("\n\033[34mDKIM Record:\033[0m")
    if dkim_record != "Record not found.":
        print("  \033[31mStatus: \033[0m\033[32mFound\033[0m")
        print("  \033[31mContent: \033[0m\033[32m", dkim_record, "\033[0m", sep='')
    else:
        print("  \033[31mStatus: \033[0m\033[95mNot found\033[0m")

    dmarc_record = get_record(f'_dmarc.{domain}', 'TXT')
    print("\n\033[34mDMARC Record:\033[0m")
    if dmarc_record != "Record not found.":
        print("  \033[31mStatus: \033[0m\033[32mFound\033[0m")
        print("  \033[31mContent: \033[0m\033[32m", dmarc_record, "\033[0m", sep='')
    else:
        print("  \033[31mStatus: \033[0m\033[94mNot found\033[0m")

    bimi_record = get_record(f'_bimi.{domain}', 'TXT')
    print("\n\033[34mBIMI Record:\033[0m")
    if bimi_record != "Record not found.":
        print("  \033[31mStatus: \033[0m\033[32mFound\033[0m")
        print("  \033[31mContent: \033[0m\033[32m", bimi_record, "\033[0m", sep='')
    else:
        print("  \033[31mStatus: \033[0m\033[94mNot found\033[0m\n")
    print("\n")
