import requests
import json
from pprint import pprint
from router_info import router

#Set REST API headers
headers = {"Accept": "application/yang-data+json", "Content-Type": "application/yang-data+json"}

url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"


#Get the response from the URL
response = requests.get(url, headers=headers, auth=(router['username'], router['password']), verify=False)

#Assign the output of response object as dictionary in api_data
api_data = response.json()

#Getting information from URL and printing using Python
print('/' * 50)
pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
print('/' * 50)
if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == 'if-state-up':
    print("Interface is Up")