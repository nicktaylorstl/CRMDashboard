import requests
import json
import keys.capsulecrm as crm

token = crm.access_token
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

# URL for GET request to view REST hook subscriptions
url = 'https://api.capsulecrm.com/api/v2/resthooks'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # If the request is successful, print the subscriptions
    subscriptions = response.json()
    print(json.dumps(subscriptions, indent=4))
    with open('subscriptions.json', 'w') as file:
        json.dump(subscriptions, file, indent=4)
else:
    # If the request failed, print the error
    print('Error:', response.status_code)
    print(response.text)
    
