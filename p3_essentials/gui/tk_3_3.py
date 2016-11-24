#!/usr/bin/python3
# You can do everything you can do with a regular button, but you can also store a value

from tkinter import *
from tkinter import ttk

root = Tk()

# Check button
checkbutton = ttk.Checkbutton(root, text='SPAM?')  # Create check button with label 'SPAM'
checkbutton.pack()  # Place button

spam = StringVar()  # Declare variable
spam.set('SPAM!')  # Assign variable to variable
print(spam.get())  # Get variable's value

# How to change the value of variable spam when checked or not checked
checkbutton.config(variable=spam, onvalue='SPAM Please!', offvalue='Boo SPAM!')  # On/off value
print(spam.get())

# Radio button
breakfast = StringVar()  # Create variable breakfast
# Create radio button with label SPAM, assign variable to control, assign value "SPAM" to variable when selected
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack()
ttk.Radiobutton(root, text='Eggs', variable=breakfast, value='Eggs').pack()
ttk.Radiobutton(root, text='Sausage', variable=breakfast, value='Sausage').pack()
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack()
print(breakfast.get())  # Note: value will be empty if no selection is made

# To change the text label on any button dynamically
checkbutton.config(textvariable=breakfast)

root.mainloop()

