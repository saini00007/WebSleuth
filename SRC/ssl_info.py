import ssl
import requests
import socket
from OpenSSL import crypto
from datetime import datetime
import sys
from colorama import Fore, Style


def get_ssl_certificate_info(url):
    # Extract hostname from the URL
    hostname = url.split('://')[1].split('/')[0]
    
    # Create a context for SSL
    context = ssl.create_default_context()
    
    try:
        # Connect to the server and get the certificate
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                certificate = ssock.getpeercert()
                if certificate is None:
                    print("Failed to retrieve SSL certificate.")
                    return
                
                # Convert the certificate to an OpenSSL X509 object
                x509 = crypto.load_certificate(crypto.FILETYPE_PEM, ssl.DER_cert_to_PEM_cert(ssock.getpeercert(True)))
                
                
                # Ensure you're working with the server's certificate
                print("====================")
       
                print(f"{Fore.BLUE}SSL certificate: {Style.RESET_ALL}{x509.get_subject().CN}")
                print("====================\n")
                # Extract and print the required information with color highlighting
                
                print(f"{Fore.RED}Subject:{Style.RESET_ALL} {x509.get_subject().CN}")
                print(f"{Fore.RED}Issuer:{Style.RESET_ALL} {x509.get_issuer().CN}")
                print(f"{Fore.RED}ASN1 Curve:{Style.RESET_ALL} {x509.get_pubkey().type()}")
                print(f"{Fore.RED}NIST Curve:{Style.RESET_ALL} {x509.get_pubkey().bits()}")
                
                expires_date = datetime.strptime(x509.get_notAfter().decode('utf-8'), '%Y%m%d%H%M%SZ')
                renewed_date = datetime.strptime(x509.get_notBefore().decode('utf-8'), '%Y%m%d%H%M%SZ')
                
                print(f"{Fore.RED}Expires:{Style.RESET_ALL} {expires_date.strftime('%d %B %Y')}")
                print(f"{Fore.RED}Renewed:{Style.RESET_ALL} {renewed_date.strftime('%d %B %Y')}")
                
                print(f"{Fore.RED}Serial Num:{Style.RESET_ALL} {x509.get_serial_number()}")
                print(f"{Fore.RED}Fingerprint:{Style.RESET_ALL} {x509.digest('sha256').decode('utf-8')}")
                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    xurl = sys.argv[1]
    #url = check_url(xurl)
    get_ssl_certificate_info(xurl)
