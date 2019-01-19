from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import string
import random
from tkinter import *
import time

random_code = ''.join(random.choice(string.digits) for i in range(5))
print(random_code)


ROOT = Tk()
LABEL = Label(ROOT, text=str(random_code))
LABEL.pack()
LOOP_ACTIVE = True

##########^^^^^#___THIS_MUST_BE_AT_THE_TOP_OF_PROGRAM___#^^^^^#############


# ENTER NEW CODE HERE
# ENTER TWILLO SEND NUMBER CODE HERE

app = Flask(__name__)

account_sid = 'AC42e108b0ca9beea35600b65013bc3d95'
auth_token = '0cb8be0e4d5c9438cac8896e09e8e4dd'
client = Client(account_sid, auth_token)
message = client.messages \
    .create(
    body="New device detected; please type in the code displayed on your screen.",
    from_='+17747736090',
    to='+15089017299'
)
print(message.sid)


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    messagereply = request.values.get('Body', None)

    resp = MessagingResponse()

    if messagereply == str(random_code):
        resp.message("Thank you!")

    else:
        resp.message("Nice Try.")

    return str(resp)


while LOOP_ACTIVE:
    ROOT.update()
    app.run()
    time.sleep(3)
    ROOT.destroy()
    LOOP_ACTIVE = False

# TWILIO END
