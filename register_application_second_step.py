import requests
import keys.capsulecrm as crm

def exchange_code_for_token(code):
    token_url = crm.token_url
    client_id = crm.client_id
    client_secret = crm.client_secret
    redirect_uri = crm.redirect_uri

    data = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code
    }

    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        return response.json()  # This contains the access token
        print(response.text)
    else:
        return None

# Use the function to get the token
token = exchange_code_for_token(crm.authorization_code)

print(token)