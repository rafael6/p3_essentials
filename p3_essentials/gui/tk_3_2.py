#!/usr/bin/python3
# button.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(root, text = "Click Me")
button.pack()

def callback():
    print('Clicked!')

button.config(command = callback)  # Map a function to a button
button.invoke()  # Programatically invoke the button

button.state(['disabled'])  # To disable a button
print(button.instate(['disabled']))  # To check if button is in disabled state
button.state(['!disabled'])  # To enable the button
print(button.instate(['!disabled']))  # To check if button is enable

logo = PhotoImage(file = 'python_logo.gif')  # Create image; change path to image as necessary
button.config(image = logo, compound = LEFT)  # Assign image to button
small_logo = logo.subsample(5, 5)  # Re-size the image
button.config(image = small_logo)  # Assign image to button

root.mainloop()
