import requests
import json
import settings
from datetime import datetime
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from utilities.item_id_ref import ITEMS_REF
from elasticsearch import Elasticsearch, helpers 

# Instanciate ES client
es = Elasticsearch()

# Instanciate Oauth2 Client & Session
client = BackendApplicationClient(client_id=settings.CLIENT_ID)
oauth = OAuth2Session(client=client)

# Getting access token from Client ID/SECRET
token = oauth.fetch_token(token_url='https://us.battle.net/oauth/token', 
    client_id=settings.CLIENT_ID,
    client_secret=settings.CLIENT_SECRET)
access_token = token['access_token']

# Making the request to auction house with defined params
data = requests.get("https://eu.api.blizzard.com/data/wow/connected-realm/"
    +str(settings.REALM_ID)+"/auctions?namespace="
    +settings.NAMESPACE+"&locale="
    +settings.LOCAL+"&access_token=" 
    + access_token).json()

# Preparing to refined object based on filter list
refined = []
scanned = 0
pushed = 0
print("SCANNING "+str(len(data['auctions']))+" ITEMS")
for d in data['auctions']:
    if d['item']['id'] in ITEMS_REF:
        # Refresh buffer for incremental bulk insert
        if len(refined) % 100 == 0:
            print(helpers.bulk(es, refined, request_timeout=1000))
            refined = []
            pushed = pushed + 100
            print("PUSHED " + str(pushed) +"/"+ str(len(data['auctions'])))
        d['_index'] = "wow-" + str(d['item']['id'])
        d['_id'] = d['id']
        d['timestamp'] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        refined.append(d)
    scanned = scanned + 1
pushed = pushed + len(refined)
print("PUSHED " + str(pushed) +"/"+ str(len(data['auctions'])))
print("SCANNED "+ str(scanned))
#print(refined)
# Write results to Elastic
print(helpers.bulk(es, refined, request_timeout=1000))
