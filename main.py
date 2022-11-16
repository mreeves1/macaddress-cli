import os
import requests
import sys

# Accepts a MAC address as an argument and sends a REST request to macaddress.io and returns the company name
# See https://macaddress.io/api/documentation/making-requests

debug = False


def main() -> str:
    if len(sys.argv) == 2:  # Expect only the filename and a single argument which should be a MAC Address
        search = sys.argv[1]
        # TODO: Add validation for MAC address
        #       Per https://macaddress.io/api/documentation/making-requests: You can use any octet delimiters including
        #       ':', '.', or even no delimiter. At least 6 BASE16 chars should be provided.

        if debug:
            print(f"MACADDRESS_API_TOKEN: {os.environ['MACADDRESS_API_TOKEN']}")
            print(f"Argument 1 of the script: {sys.argv[1]}")

        if "MACADDRESS_API_TOKEN" in os.environ:
            api_token = os.environ['MACADDRESS_API_TOKEN']
            output = "vendor"  # when output = vendor, company name is returned
            url = f"https://api.macaddress.io/v1?output={output}&search={search}"
            headers = {'X-Authentication-Token': api_token}
            r = requests.get(url, headers=headers)
            if r.status_code != 200:
                print("The API call to api.macaddress.io failed!")
                print(f"Response Code: {r.status_code}")
                print(f"Error Trace: {r.raise_for_status()}")
                sys.exit(1)
            else:
                return r.text
        else:
            print("Please set your MACADDRESS_API_TOKEN environment variable.")
            print("The API Token will be found at https://macaddress.io/account/general.")
            sys.exit(2)

    else:
        print("""
            Setup:
                Create account at https://macaddress.io/signup
                Then go to https://macaddress.io/account/general save your API token to an env var: MACADDRESS_API_TOKEN
                export MACADDRESS_API_TOKEN=REDACTED

            Usage: 
                python main.py 44:38:39:ff:ef:57
                OR
                docker build -t macaddress-cli .
                docker run -e MACADDRESS_API_TOKEN macaddress-cli 44:38:39:ff:ef:57
        """)
        sys.exit(3)


if __name__ == '__main__':
    print(main())
else:
    print("This is meant to be run directly and never imported.")
    sys.exit(4)
