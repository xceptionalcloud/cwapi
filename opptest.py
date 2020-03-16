import requests
import configparser
import base64

#AUTHENTICATION STAGING
config = configparser.RawConfigParser()
config.read('/var/www/settings.ini')
cwaClientId = config['CW']['clientid']
cwaAuth = config['CW']['auth']
workCounter = 0
workMax = 1000

test = base64.b64decode(str(cwaAuth))
print(test)

#GET EXAMPLE
'''
cwaTixReq = requests.get("https://api-na.myconnectwise.net/v4_6_release/apis/3.0/service/tickets",
    headers={'Authorization': str(cwaAuth), 'Accept': 'application/json', 'clientId': str(cwaClientId)})
'''
cwaOppReq = requests.get("https://api-na.myconnectwise.net/v4_6_release/apis/3.0/sales/opportunities",
    headers={'Authorization': str(cwaAuth), 'Accept': 'application/json', 'clientId': str(cwaClientId)})

for entry in cwaOppReq.json():
    if workCounter < workMax:
        workCounter+=1
        print(entry['id'])
