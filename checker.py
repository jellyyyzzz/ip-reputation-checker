import os
import requests
from dotenv import load_dotenv

#Load API key from .env
load_dotenv()
API_KEY = os.getenv("ABUSEIPDB_API_KEY")

def check_ip_reputation(ip_address: str):
    """Check IP reputation using AbuseIPDB API"""
    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Accept": "application/json",
        "Key": API_KEY
    }

    params = {
        "ipAddress": ip_address,
        "MaxAgeInDays": 90 #last 90-days report
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return

    data = response.json()["data"]

    print("\n---IP Reputation Report---")
    print(f"IP Address: {data['ipAddress']}")
    print(f"Abuse Confidence Score: {data['abuseConfidenceScore']} / 100")
    print(f"Total Reports: {data['totalReports']}")
    print(f"Last Reported At: {data.get('lastReportedAt'), 'N/A'}")
    print(f"Country: {data.get('countryCode'), 'N/A'}")
    print(f"ISP: {data.get('isp', 'N/A')}")
    print(f"Domain: {data.get('domain'), 'N/A'}")
    print(f"Usage Type: {data.get('usageType', 'N/A')}")

    if data['abuseConfidenceScore'] > 50:
        print("This IP has a high abuse confidence score. Potentially malicious")
    elif data['abuseConfidenceScore'] > 0:
        print("This IP has some reports. Caution advised")
    else:
        print("This IP appears clean.")

if __name__=="__main__":
    ip = input("Enter IP address to check: ").strip()
    check_ip_reputation(ip)
