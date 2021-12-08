
import requests
import json
import time
from Get_auth_tokern import get_token


def main():

    token = get_token()
    api_path= "https://sandboxdnac.cisco.com/dna"
    #payload={}
    headers = {'Content-Type': 'application/json','X-Auth-Token': token }





    new_device_dict = {
        "ipAddress": ["192.0.2.1"],
        "snmpVersion": "v2",
        "snmpROCommunity": "readonly",
        "snmpRWCommunity": "readwrite",
        "snmpRetry": "1",
        "snmpTimeout": "60",
        "cliTransport": "ssh",
        "userName": "nick",
        "password": "secret123!",
        "enablePassword": "secret456!",
    }

    add_resp = requests.post(f"{api_path}/intent/api/v1/network-device" , json=new_device_dict, headers=headers)

    if add_resp.ok:
        #wait for 10 seconds after server responds 
        print (f"request accepted : status code {add_resp.status_code}")
        time.sleep(10)

        # DNAC will responds with task ID 
        task = add_resp.json()["response"]["taskId"]
        task_resp = requests.get ( f"{api_path}/intent.api.v1/task/{task}" , headers=  headers)


    # See if the task was completed successfully or not
        if task_resp.ok:
            task_data = task_resp.json()["response"]
            if not task_data["isError"]:
                print("New device successfully added")
            else:
                print(f"Async task error seen: {task_data['progress']}")
        else:
            print(f"Async GET failed: status code {task_resp.status_code}")

    else:
        # The initial HTTP POST failed; print details
        print(f"Device addition failed with code {add_resp.status_code}")
        print(f"Failure body: {add_resp.text}")


if __name__ == "__main__":
    main()

