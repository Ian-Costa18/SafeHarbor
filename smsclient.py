from tkinter import *
import threading
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from string import digits as string_digits
from random import choice as random_choice
import devicefunctions

class App(threading.Thread):

    def __init__(self, tk_root):
        self.root = tk_root
        threading.Thread.__init__(self)
        self.start()
        self.auth = False
        self.random_num = ''.join(random_choice(string_digits) for i in range(5))

    def run(self):
        web_app = Flask(__name__)
        account_sid = 'AC42e108b0ca9beea35600b65013bc3d95'
        auth_token = '0cb8be0e4d5c9438cac8896e09e8e4dd'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="New device detected; please type in the code displayed on your screen.",
            from_='+17747736090',
            to='+14013323971')
        print(message.sid)

        @web_app.route("/sms", methods=['GET', 'POST'])
        def incoming_sms():
            """Send a dynamic reply to an incoming text message"""
            messagereply = request.values.get('Body', None)

            resp = MessagingResponse()

            if messagereply == str(self.random_num):
                resp.message("Thank you!")
                self.auth = True

            else:
                resp.message("Nice Try.")

            return resp

        web_app.run()
        self.root.quit()
        self.root.update()

def startclient():
    ROOT = Tk()
    APP = App(ROOT)
    labela = Label(text="Here is your 5 digit code:", font=("Courier New", 16))
    labela.pack()
    labelb = Label(text="%s" % APP.random_num, font=("Courier New", 30))
    labelb.pack()
    ROOT.mainloop()

    return APP
