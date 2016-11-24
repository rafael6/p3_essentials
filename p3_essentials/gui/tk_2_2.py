#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

root = Tk()  # Creates the main canvas

button = ttk.Button(root, text = 'Click Me')  # Create a button with text on it
button.pack()  # Displays the button

print(button['text'])  # Prints the value of text on the button
button['text'] = 'Press Me'  # To change the text on the button property
button.config(text = 'Push Me')  # Another way to change the text property
print(button.config())  # To print all the properties if the widget as a dict

print(str(button))  # To display the underline tk name used by tk
print(str(root))  # To display the underline name of the root (.)

ttk.Label(root, text ='Hello, Tkinter!').pack()  # create a label without a variable reference.

# mainloop() add
root.mainloop()

