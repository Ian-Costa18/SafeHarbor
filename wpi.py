import tkinter
from tkinter import *
import string
import random

def code():
    #Top Level

    #ENTER TWILLO SEND NUMBER CODE HERE
    pineapple=(phone_number.get())
    apple=("+1%s" %pineapple)
    print(apple)
    top=Toplevel()
    top.title=("Code Generator")
    
    labela=Label(top, text="Here is your 5 digit code:", font=("Courier New",16))
    labela.pack()

    random_code=''.join(random.choice(string.digits) for i in range(5))
    print(random_code)

    labelb=Label(top, text="%s" %random_code, font=("Courier New",30))
    labelb.pack()
    
##########^^^^^#___THIS_MUST_BE_AT_THE_TOP_OF_PROGRAM___#^^^^^#############






#ENTER NEW CODE HERE







####################___ROOT_LEVEL___#######################################
#########___THIS_MUST_BE_AT_THE_BOTTOM_OF_PROGRAM___#######################
root=Tk()

root.title("Security Clearence")

label1=Label(root, text="Please enter your phone number below.\nNo - between numbers please.", font=("Courier New",13))
label1.pack()

phone_number=Entry(root)
phone_number.pack()

button1=Button(root, text="Enter", command=code)
button1.pack()

root.geometry("400x200")

root.mainloop()
