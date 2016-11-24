#!/usr/bin/python3
# entry.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root, width=30)  # Display entry field for 30 characters, no input limit
entry.pack()

entry.get()  # To get a str object of the content in the entry field


entry.delete(0, 1)  # To delete first character like [0:1]
entry.delete(0, END)  # To delete the entire content of the entry field
entry.insert(0, 'Enter your password')  # To put this text in entry field starting from character one

entry.config(show='*')  # As user type character replaced with *; entry.get() gets the real chars
entry.state(['disabled'])  # Grayed-out
entry.state(['readonly'])  # Useful when generating something for user to copy.
entry.state(['!disabled'])  # To disable it

root.mainloop()

