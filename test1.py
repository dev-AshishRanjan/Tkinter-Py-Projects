import requests
import json

api_request=requests.get("http://api.weatherstack.com/current?access_key=57c8daa000c7c60a7ce6b98a31933429&query=Muzaffarpur")
api=json.loads(api_request.content)
p=api["location"]
print(p)
for k in p:
    print(f"{k} : {p[k]}")