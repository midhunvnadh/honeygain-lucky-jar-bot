import json
import requests
import datetime
from time import sleep

def getAuth():
	auth = open("auth.txt", "r").read()
	auth = auth.replace('\n','')
	auth = auth.replace('\t','')
	return auth

def getHeaders():
	return json.loads(open("./headers.json", 'r').read())

def main():
    api_url = "https://dashboard.honeygain.com/api/v1/contest_winnings"
    headers = getHeaders()
    
    headers["authorization"] = "Bearer " + getAuth()

    r = requests.post(url=api_url, headers=headers)
    print(f"Bot ran on {datetime.datetime.now()}: {r.text}")


while True:
    main();
    sleep(60 * 60 * 6) # Every 6 hours
