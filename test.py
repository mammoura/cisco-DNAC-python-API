


import requests
import json

from Get_auth_tokern import get_token

# Get the device list from DNAC

def main():

    
    
    token = get_token()
    api_path= "https://sandboxdnac.cisco.com/dna"
    #payload={}
    headers = {
    'Content-Type': 'application/json',
    'X-Auth-Token': token
    }

    response = requests.get( f"{api_path}/intent/api/v1/network-device", headers=headers)

    for device in response.json()["response"]:
      print(device['hostname'], device['managementIpAddress'])
   


if __name__ == "__main__":
    main()



