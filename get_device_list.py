


import requests
import json

from Get_auth_tokern import get_token

# Get the device list from DNAC

def main():

    #url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/"
    
    token = get_token()
    api_path= "https://sandboxdnac.cisco.com/dna"
    #payload={}
    headers = {
    'Content-Type': 'application/json',
    'X-Auth-Token': token
    }

    response = requests.get( f"{api_path}/intent/api/v1/network-device", headers=headers)

    #print(response.text)
    #ip_list = json.dumps(response.json(), indent=2)
    
    #
    #print(ip_list)

    if response.ok:
        for device in response.json()["response"]:
            print(f"ID:{device['id']}   IP: {device['managementIpAddress']}"  )

    else:
        print (f"Device collection fails with code {response.status_code}")
        print (f"Failure body: {response.text}")



if __name__ == "__main__":
    main()



