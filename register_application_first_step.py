import webbrowser
import keys.capsulecrm as crm

# Define the necessary parameters
client_id = crm.client_id  # Replace with your client ID


# Construct the authorization URL
auth_url = f"https://api.capsulecrm.com/oauth/authorise?response_type=code&client_id={client_id}"

# Redirect the user to the authorization URL
webbrowser.open(auth_url)