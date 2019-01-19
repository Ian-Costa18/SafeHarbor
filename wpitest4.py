from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import tkinter
from tkinter import *
import string
import random


random_code = ''.join(random.choice(string.digits) for i in range(5))
print(random_code)


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
    to='+19734400514'
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
if __name__ == "__main__":
        app.run()



# TWILIO END

root = Tk()

root.title("Security Clearance")

labela = Label(root, text="Here is your 5 digit code:", font=("Courier New", 16))
labela.pack()

labelb = Label(root, text="%s" % random_code, font=("Courier New", 30))
labelb.pack()


root.geometry("400x200")

root.mainloop()