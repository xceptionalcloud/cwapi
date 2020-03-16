import requests
import configparser
import base64

#AUTHENTICATION STAGING
config = configparser.RawConfigParser()
config.read('/var/www/settings.ini')
cwaClientId = config['CW']['clientid']
cwaAuth = config['CW']['auth']
cwaUrlPre = 'https://api-na.myconnectwise.net/v4_6_release/apis/3.0/'
cwaApiType = 'sales/opportunities/'
cwaApiCall = 'count'
cwaOppId = '6273'

workCounter = 0
workMax = 1000


cwaApiUrl = cwaUrlPre + cwaApiType + cwaApiCall
print(cwaApiUrl)
#GET EXAMPLE
#cwaTixReq = requests.get(cwaApiUrl, headers={'Authorization': str(cwaAuth), 'Accept': 'application/json', 'clientId': str(cwaClientId)})
cwaOppReq = requests.get(str(cwaApiUrl), headers={'Authorization': str(cwaAuth), 'Accept': 'application/json', 'clientId': str(cwaClientId)})
#cwaOppReq = requests.get(cwaApiUrl, headers={'Authorization': str(cwaAuth), 'Accept': 'application/json', 'clientId': str(cwaClientId)})

thisTicket = cwaOppReq.json()
print(thisTicket)
