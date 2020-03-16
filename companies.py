import requests
import configparser
import base64

workCounter = 0
workMax = 10000

#AUTHENTICATION STAGING
config = configparser.RawConfigParser()
config.read('/var/www/settings.ini')
cwaClientId = config['CW']['clientid']
cwaAuth = config['CW']['auth']
cwaUrlPre = 'https://api-na.myconnectwise.net/v4_6_release/apis/3.0/'
cwaApiType = 'company/companies/'
#cwaApiType = 'sales/opportunities/'
cwaOppId = '6273'
cwaApiCall = ''
cwaApiParamPre = '?'
cwaPages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
pageSize = 500
response = ''

for page in cwaPages:
    iterator = 0
    cwaApiParams = {'pageSize': str(pageSize), 'page': str(page)}
    cwaApiParamPkg = ''
    for entry, value in cwaApiParams.items():
        iterator+=1
        if iterator == len(cwaApiParams):
            cwaApiParamPkg = str(cwaApiParamPkg) + str(entry) + '=' + str(value)
        else:
            cwaApiParamPkg = str(cwaApiParamPkg) + str(entry) + '=' + str(value) + '&'
    cwaApiParamFinal = cwaApiParamPre + cwaApiParamPkg
    cwaApiUrl = cwaUrlPre + cwaApiType + cwaApiCall + cwaApiParamFinal
    print(cwaApiUrl)
    cwaOppReq = requests.get(str(cwaApiUrl), headers={'Authorization': str(cwaAuth), 'Accept': 'application/json', 'clientId': str(cwaClientId)})
    response = cwaOppReq.json()
    print(len(response))
    if len(response) != pageSize:
        break
print('done')
