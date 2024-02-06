import requests
from requests.auth import HTTPBasicAuth
import json
from google.cloud import bigquery
import os
import pytest
import keys.google as gg 
import keys.upstash as upstash

#https://us-central1-crmdashboardmlb.cloudfunctions.net/consumer
def consumer_api_get():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'keys/googleapikey.json'
    
    endpoint_url = upstash.endpoint_url
    group_id = upstash.group_id
    topic = upstash.topic

    url = f"{endpoint_url}/consume/{group_id}/GROUP_INSTANCE_NAME/{topic}"


    username = upstash.username
    password = upstash.password

    headers = {
        "Kafka-Auto-Offset-Reset": "earliest"
    }

    def send_to_google(message):
            # Construct a BigQuery client object.
        client = bigquery.Client()
        table_id = gg.table_id
        #message_str = message.value.decode('utf-8')
        rows_to_insert = [message]

        errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
        if errors == []:
            print("New rows have been added.")
        else:
            print("Encountered errors while inserting rows: {}".format(errors))

    # Make the GET request
    response = requests.get(url, headers=headers, auth=HTTPBasicAuth(username, password))
    print(response.status_code)
    print(response.content)
    json_string = response.content.decode('utf-8').strip()
    response_list = json.loads(json_string)
    opportunities = []
    
    for dict in response_list:
            value = str(dict["value"])
            timestamp = dict["timestamp"]/1000.0
            opportunities.append({"timestamp":timestamp,"value":value})


    # Check if the request was successful
    if response.status_code == 200:
        print("Success:")
        print(type(opportunities))
        print(opportunities)
        for item in opportunities:
            send_to_google(item)
    else:
        print("Error:", response.status_code, response.text)

consumer_api_get()


