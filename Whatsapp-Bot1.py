#################################################################################################
## This is a Flask application used to receive message from Whatsapp via Twilio API          	#
## , raise ticket in ServiceNow based on message received and then response back to				# 
## Whatsapp user via Twilio api with the status code of the rest api call.						#
#################################################################################################

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
app = Flask(__name__)


@app.route("/")
def apphome():
    return "Welcome back!!"


@app.route("/sms", methods=['POST'])

def sms_reply():
    msg = request.form.get('Body')
    url = "https://techmnonprod2.service-now.com/api/now/table/incident"
    user = "farman.k"
    passwd = "farman@word1"
    authen = (user, passwd)
    header = {"Content-type": "Application/Json", "Accept": "Application/Json"}
    body = "{\"short_description\": " + "\"" + msg + "\"}"
    response = requests.post(url, auth=authen, headers=header, data=body)
    #print(response.status_code)
    resp = MessagingResponse()
    resp.message("Hey, Farman You said: {0} with status: {1}".format(msg, response.status_code))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)