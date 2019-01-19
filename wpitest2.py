import tkinter
from tkinter import *
import string
import random


root = Tk()

root.title("Security Clearence")


labela = Label(root, text="Here is your 5 digit code:", font=("Courier New", 16))
labela.pack()

random_code = ''.join(random.choice(string.digits) for i in range(5))
print(random_code)

labelb = Label(root, text="%s" % random_code, font=("Courier New", 30))
labelb.pack()


root.geometry("400x200")

root.mainloop()
