import ssl
import socket
import sys
def get_cipher_suites_info(url):
    try:
        hostname = url.split('/')[2]
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cipher_suites = ssock.cipher()
            
                ssl_info = ssock.getpeercert()
                
                key_exchange = ssl_info.get('keyExchange', 'Unknown')
                return {
                    "Cipher Name": cipher_suites[0],
                    "TLS Version": cipher_suites[1],
                    "Key Exchange Protocol": key_exchange,
                    "Public Key Algorithm": ssl_info.get('pubkeyType', 'Unknown'),
                    "Signature Algorithm": ssl_info.get('signatureAlgorithm', 'Unknown'),
                    "Session Ticket Supported": ssl_info.get('session_ticket_supported', False),
                    "OCSP Stapling Supported": ssl_info.get('ocsp_response', False),
                    "Perfect Forward Secrecy": cipher_suites[2],
                    "Elliptic Curves Supported": ssl_info.get('ecdh_nid', 'No')
                }
    except Exception as e:
        print(f"Error: {e}")
        return None

url = sys.argv[1]
print("\033[0m====================")
print( "\033[34mTLS Cipher Suites \033[0m" )
print("====================\n")
cipher_info = get_cipher_suites_info(url)
if cipher_info:
    for key, value in cipher_info.items():
        print(f"\033[31m{key}: \033[32m{value}")
    print("\n")
