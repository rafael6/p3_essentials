#!/usr/bin/python3
# label.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root, text = "Hello, Tkinter!")
label.pack()
label.config(text = 'Howdy, Tkinter!')
label.config(text = 'Howdy, Tkinter! It\'s been a really long time since we last met.  Great to see you again!')
label.config(wraplength = 150)
label.config(justify = CENTER)
label.config(foreground = 'blue', background = 'yellow')
label.config(font = ('Courier', 18, 'bold'))
label.config(text = 'Howdy, Tkinter!')

logo = PhotoImage(file = 'python_logo.gif') # change path to image as necessary

# If used in a function, the iamage will go out of scope
label.config(image = logo)

# To avoid going out of scope, assign image to label
label.img = logo
label.config(image = label.img)

label.config(compound = 'text')
label.config(compound = 'center')
label.config(compound = 'left')



root.mainloop()

