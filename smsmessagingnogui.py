""" SMS module for authentication"""
from string import digits as string_digits
from random import choice as random_choice
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from devicefunctions import unlock_device

def start_sms():
    """ Starts SMS service"""

    # Generate 5 character random number for authentication
    random_num = ''.join(random_choice(string_digits) for i in range(5))
    print(random_num)
    # Create flask server for twilio
    app = Flask(__name__)
    # Create twilio client
    account_sid = 'AC42e108b0ca9beea35600b65013bc3d95'
    auth_token = '0cb8be0e4d5c9438cac8896e09e8e4dd'
    client = Client(account_sid, auth_token)
    # Craft text message
    message = client.messages.create(
        body="New device detected; please type in the code displayed on your screen.",
        from_='+17747736090',
        to='+14017719495'
    )
    print(message.sid)

    # Create listener for incoming sms messages, route through (ip)/sms
    @app.route("/sms", methods=['GET', 'POST'])
    def incoming_sms():
        """Send a dynamic reply to an incoming text message"""
        messagereply = request.values.get('Body', None)

        resp = MessagingResponse()

        # If both the message and random number are the same approve auth
        if messagereply == str(random_num):
            resp.message("Thank you!")
            print(resp)
            unlock_device('*')
            return str(resp)

        # Deny everything else
        else:
            resp.message("Try again.")
            print(resp)
            return str(resp)
    # Run flask server
    app.run()

if __name__ == "__main__":
    start_sms()
