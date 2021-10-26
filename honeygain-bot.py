import json
import requests
import datetime
from time import sleep


def getAuth():
    auth = open("auth.txt", "r").read()
    auth = auth.replace('\n', '')
    auth = auth.replace('\t', '')
    return auth


def getHeaders():
    return json.loads(open("./headers.json", 'r').read())


def main():
    api_url = "https://dashboard.honeygain.com/api/v1/contest_winnings"
    headers = getHeaders()

    headers["authorization"] = "Bearer " + getAuth()

    r = requests.post(url=api_url, headers=headers)
    print(f": {r.text}")


while True:
    print(f"Bot ran on {datetime.datetime.now()}", end="")
    try:
        main()
    except:
        print("Some sort of error occoured!")
    sleep(60 * 60 * 2)  # Every 2 hours
