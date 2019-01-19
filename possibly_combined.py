from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import tkinter
from tkinter import *
import string
import random


def code():
    # Top Level
    pineapple = (phone_number.get())
    length_pineapple = len(pineapple)
    print(length_pineapple)
    apple = ("+1%s" % pineapple)
    print(apple)
    top = Toplevel()
    top.title = ("Code Generator")

    if len(pineapple) != 10:
        top.destroy()
        label2 = Label(root, text="Error: Invalid Phone Number")
        label2.pack()

    labela = Label(top, text="Here is your 5 digit code:", font=("Courier New", 16))
    labela.pack()

    random_code = ''.join(random.choice(string.digits) for i in range(5))
    print(random_code)

    labelb = Label(top, text="%s" % random_code, font=("Courier New", 30))
    labelb.pack()


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

    if __name__ == "__main__":
        app.run()


# TWILIO END

####################___ROOT_LEVEL___#######################################
#########___THIS_MUST_BE_AT_THE_BOTTOM_OF_PROGRAM___#######################
root = Tk()

root.title("Security Clearence")

label1 = Label(root, text="Please enter your phone number below.\nNo - between numbers please.",
               font=("Courier New", 13))
label1.pack()

phone_number = Entry(root)
phone_number.pack()

button1 = Button(root, text="Enter", command=code)
button1.pack()

root.geometry("400x200")

root.mainloop()
