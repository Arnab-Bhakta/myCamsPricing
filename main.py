import scrapper
import gmailclient
import json

with open('secrets.json') as json_data:
    secrets = json.load(json_data)
scrapper.scrapper(float(secrets['units']))
gmailclient.gmail_client(secrets['sender'], secrets['receiver'])
