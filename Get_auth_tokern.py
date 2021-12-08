
import requests

# Get an Auth token from cisco dna sandbox


def get_token():


    #defin the api path and basic auth 

    api_path= "https://sandboxdnac.cisco.com/dna"
    auth = ("devnetuser","Cisco123!")
    headers = {"Content-Type": "application/json"}

    #Issue HTTP post requst to the proper URL to request token

    auth_resp = requests.post(
        f"{api_path}/system/api/v1/auth/token", auth=auth, headers=headers
    )


    #If successful, print token , else , rais HTTP Error with details

    auth_resp.raise_for_status()
    token = auth_resp.json()["Token"]

    return token


def main():
    """
    Execution begins here.
    """

    token = get_token()
    print(token)


if __name__ == "__main__":
    main()