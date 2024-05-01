import dns.resolver
from urllib.parse import urlparse

def get_dns_records(url):
    try:
        # Parse the URL to extract the domain name
        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        # Perform DNS resolution
        answers = dns.resolver.resolve(domain, 'A')
        # Extract and print A Records (IPv4 addresses)
        print("A Records (IPv4 addresses):")
        ip_addresses_v4 = [answer.address for answer in answers]
        for address in ip_addresses_v4:
            print(address)

        answers = dns.resolver.resolve(domain, 'AAAA')
        # Extract and print AAAA Records (IPv6 addresses)
        print("\nAAAA Records (IPv6 addresses):")
        ip_addresses_v6 = [answer.address for answer in answers]
        for address in ip_addresses_v6:
            print(address)

        try:
            answers = dns.resolver.resolve(domain, 'MX')
            # Extract and print MX Records (Mail exchange)
            print("\nMX Records (Mail exchange):")
            for answer in answers:
                print(answer.exchange)
        except dns.resolver.NoAnswer:
            print("\nNo MX Records found for", domain)

        try:
            answers = dns.resolver.resolve(domain, 'SOA')
            # Extract and print SOA Records (Start of Authority)
            print("\nSOA Records (Start of Authority):")
            for answer in answers:
                print(answer)
        except dns.resolver.NoAnswer:
            print("\nNo SOA Records found for", domain)

        return ip_addresses_v4, ip_addresses_v6

    except Exception as e:
        print("Error:", str(e))
        return [], []

# Example usage
url = input("Enter the URL: ")
get_dns_records(url)
