import requests
import configparser

#AUTHENTICATION STAGING
config = configparser.RawConfigParser()
config.read('/var/www/settings.ini')
cwaClientId = config['CW']['clientid']
cwaAuth = config['CW']['auth']
print(cwaClientId)
#GET EXAMPLE
cwaReq = requests.get("https://api-na.myconnectwise.net/v4_6_release/apis/3.0/service/tickets",
    headers={'Authorization': str(cwaAuth), 'Accept': 'application/json', 'clientId': str(cwaClientId)})
print(cwaReq.text)
'''
if(getRC.equals(200)) {
    print(cwExampleGet.getInputStream().getText())
}
else {
	print("Code was - " + getRC)
	try {
		print(cwExampleGet.getInputStream().getText())
	}
	catch(connEx) {
		print("Failed to rec'v stream")
	}
}
'''
