import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth

USER = input('Enter your username for DNAC: ')
PASS = getpass('Enter your password for DNAC: ')

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

baseurl = 'https://sandboxdnac.cisco.com'
authAPI = "/dna/system/api/v1/auth/token"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
 }

dnaAuth = baseurl + authAPI

response = requests.post(dnaAuth, auth=HTTPBasicAuth(USER, PASS), headers=headers, data=payload)

print(response.text)
