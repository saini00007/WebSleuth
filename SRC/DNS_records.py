import aiohttp
import asyncio
import json
import sys
async def fetch_dns_records(domain):
    try:
        async with aiohttp.ClientSession() as session:
            url = f"https://api.whoisfreaks.com/v2.0/dns/live?apiKey=bac036a63ee74c3698be8bc85fbefdef&domainName={domain}&type=all"
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text()
    except aiohttp.ClientError as e:
        print(f"An error occurred: {e}")
        return None

def format_dns_output(json_data):
    formatted_output = "\n"
    try:
        data = json.loads(json_data)
        for record in data['dnsRecords']:
            formatted_output += f"\033[31mDNS Type:\033[32m {record['dnsType']}\n"  # Red color for keys
            formatted_output += f"\033[31mTTL:\033[32m {record['ttl']}\n"  # Green color for values
            formatted_output += f"\033[31mRaw Text:\033[32m {record['rawText']}\n"
            formatted_output += f"\033[31mRRset Type:\033[32m {record['rRsetType']}\n"
            formatted_output += f"\033[31mAddress:\033[32m {record.get('address', 'N/A')}\n\n"
    except json.JSONDecodeError as e:
        print(f"Unable to get DNS records")
    return formatted_output

async def main():
    domain = sys.argv[1]
    dns_data = await fetch_dns_records(domain)
    if dns_data:
        formatted_output = format_dns_output(dns_data)
        print(formatted_output)

if __name__ == "__main__":
    print("\033[0m====================")
    print( "\033[34mDns Records \033[0m" )
    print("====================\n")
    asyncio.run(main())
