# ip-reputation-checker

## Project Overview
**IP Reptutation Checker** is a Python-based tool that uses the [AbuseIPDB API](https://www.abuseipdb.com/api) to analyze the reputation and threat level of a given IP address.
It checks for reported abuse, country of origin, ISP, and usage type - helping security analysts identify potentially **malicious or suspicious IPs**.

---

## Features
- Fetch Ip reputation data from **AbuseIPDB**
- Displays abuse confidence score and report count
- Shows ISP, domain, usage type, and geolocation info
- Provides human-readable threat evaluation
- Lightweight, simple, and API-based

---

## Installation
Install the dependencies using:
'''bash
pip install requests python-dotenv

## Setup/API Instructions
Visit https://www.abuseipdb.com/register
Sign up/Log in to get your API key
