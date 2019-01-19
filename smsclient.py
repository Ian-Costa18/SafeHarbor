from tkinter import *
import threading
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import string
import random

random_code = ''.join(random.choice(string.digits) for i in range(5))
print(random_code)


class App(threading.Thread):

    def __init__(self, tk_root):
        self.root = tk_root
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        loop_active = True
        while loop_active:
            user_input = 0
            if user_input == 0:
                loop_active = False
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

                if __name__ == "__main__":
                    app.run()
                    self.root.quit()
                    self.root.update()
            else:
                print("You're not supposed to be here...")


ROOT = Tk()
APP = App(ROOT)
labela = Label(text="Here is your 5 digit code:", font=("Courier New", 16))
labela.pack()
labelb = Label(text="%s" % random_code, font=("Courier New", 30))
labelb.pack()


ROOT.mainloop()
