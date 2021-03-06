import groovy.json.JsonSlurper
import static java.util.Calendar.*

//AUTHENTICATION STAGING
def authPath = '/home/xndev/opsroot/credentials/'
def cwAuthFile = authPath + 'cw.txt'
def cwClientIdFile = authPath + 'cw-clientid.txt'
def cwAuthText = new File(cwAuthFile).getText().trim()
def cwClientId = new File(cwClientIdFile).getText().trim()

// GET EXAMPLE
def cwExampleGet = new URL("https://api-na.myconnectwise.net/v4_6_release/apis/3.0/service/tickets/54022").openConnection() as HttpURLConnection
cwExampleGet.setRequestProperty( 'Authorization', cwAuthText )
cwExampleGet.setRequestProperty( 'Accept', 'application/json' )
cwExampleGet.setRequestProperty( 'clientId', cwClientId )

def getRC = cwExampleGet.getResponseCode()
log.info(getRC)
if(getRC.equals(200)) {
	def cwResponseJson = cwExampleGet.getInputStream().getText()
	log.info(cwResponseJson)
	def cwResponseParsed = new JsonSlurper().parseText(cwResponseJson)
	log.info(idEntry)
}
else {
	log.info("Code was - " + getRC)
	try {
		log.info(cwResponseJson)
	}
	catch(connEx) {
		log.info("Failed to rec'v stream")
	}
}

/*
// POST
def post = new URL("https://httpbin.org/post").openConnection();
def message = '{"message":"this is a message"}'
post.setRequestMethod("POST")
post.setDoOutput(true)
post.setRequestProperty("Content-Type", "application/json")
post.getOutputStream().write(message.getBytes("UTF-8"));
def
*/
