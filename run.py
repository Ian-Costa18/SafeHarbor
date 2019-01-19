from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import random


app = Flask(__name__)

randomnum = str(random.randint(10000, 90000))


account_sid = 'AC42e108b0ca9beea35600b65013bc3d95'
auth_token = '0cb8be0e4d5c9438cac8896e09e8e4dd'
client = Client(account_sid, auth_token)
message = client.messages \
    .create(
    body="This is a test. Please reply with - " + randomnum,
    from_='+17747736090',
    to='+15089017299'
)
print(message.sid)


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    messagereply = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if messagereply == str(randomnum):
        resp.message("Thank you!")

    else:
        resp.message("Nice Try.")

    return str(resp)


if __name__ == "__main__":
    app.run()
