import scrapper
import gmailclient
import json
import datetime

with open('secrets.json') as json_data:
    secrets = json.load(json_data)
scrapper.scrapper(float(secrets['units']))
print( str( datetime.datetime.now() ) + " : " )
gmailclient.gmail_client(secrets['sender'], secrets['receiver'])

