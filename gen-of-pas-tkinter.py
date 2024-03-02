import random
from tkinter import *

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!№;%:?*()_+-=.,/?|\';:}]{[@#$%^&"

length = 8

def generatepassword():
    password = "".join(random.sample(characters, length))
    label.config(text=password)
    
window = Tk()

window.title('Password Generator')

generatebtn = Button(window,text="Click to Generate Password",command=generatepassword)
generatebtn.pack()

label = Label (window,text="")

label.pack(padx = 200, pady = 50)

window.mainloop()

