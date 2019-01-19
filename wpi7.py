from tkinter import *
import random
import string

root = Tk()
randomnum=''.join(random.choice(string.digits) for i in range(5))
w = Label(root, text="%s" %randomnum)
w.pack()
root.mainloop()
