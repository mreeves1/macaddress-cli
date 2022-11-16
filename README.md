# macaddress-cli

## Overview
Accepts a MAC address as an argument and sends a REST request to macaddress.io and returns the company name.

## Setup

1. Go to https://macaddress.io/signup and create a free account
2. Validate the account in your email and then login
3. Go to https://macaddress.io/account/general and save your API key into an environment variable named MACADDRESS_API_TOKEN

## Running
```
export MACADDRESS_API_TOKEN=at_REDACTED
docker build -t macaddress-cli .
docker run -e MACADDRESS_API_TOKEN macaddress-cli 44:38:39:ff:ef:57
```

## Development

Use a virtual env to develop. These instructions work in "git-bash" running on Windows so will be different on linux/mac. See https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/ if you need tips.

```
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
```

Then you can edit main.py and run it locally via:
```
python main.py 44:38:39:ff:ef:57
```

## Future Enhancements

* Make a simple bash wrapper script so user's don't need to run the docker build/run commands directly, validates docker is installed, etc.

* Add some tests