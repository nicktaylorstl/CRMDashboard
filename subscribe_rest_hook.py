import requests
import json
import keys.capsulecrm as crm
import keys.upstash as upstash

token = crm.access_token
target_url = upstash.resthook_url
headers = {'Authorization':f'Bearer {token}','Content-Type': 'application/json'}


def subscribe_rest_hook(opportunity_type):
# Possible opportunity types (updated,closed,deleted,created)
    data = {
        "restHook" : { 
        "event" : f"opportunity/{opportunity_type}",
        "targetUrl" : target_url,
        "description" : opportunity_type
        }
    }
    response = requests.post('https://api.capsulecrm.com/api/v2/resthooks', json=data, headers=headers)
    if response.status_code == 201:
        print(f'{opportunity_type} subscription successful')
    else:
        print('Error:', response.status_code)
        print(response.text)

opportunities = ["updated","closed","deleted","created"]
for type in opportunities:
    subscribe_rest_hook(type)
