import os
from os import path
import datetime
import time


# OS type
print('The OS type is: {}'.format(os.name))

# Path variable
print('The path variable is: {}'.format(os.getenv('PATH')))

# Current working directory
print('Current working directory is: {}'.format(os.getcwd()))

# Random strings
print('A 25 bytes long string: {}'.format(os.urandom(25)))

# Check for item existence and type
print ("Item exists: " + str(path.exists("textfile.txt")))
print ("Item is a file: " + str(path.isfile("textfile.txt")))
print ("Item is a directory: " + str(path.isdir("textfile.txt")))

# Work with file paths
print ("Item's path: " + str(path.realpath("textfile.txt")))
print ("Item's path and name: " + str(path.split(path.realpath("textfile.txt"))))

# rename file
os.rename("textfile.txt", "newfile.txt")

# path where this file exists
print(os.path.abspath(__file__))

# one dir up from path where this (os_module.py) exists
print(os.path.dirname(os.path.abspath(__file__)))

# two dirs up from path where this (os_module.py) exists
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Get the modification time
t = time.ctime(path.getmtime("textfile.txt"))
print (t)
print (datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

# Calculate how long ago the item was modified
td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
print ("It has been " + str(td) + " The file was modified")
print ("Or, " + str(td.total_seconds()) + " seconds ago.")

# More OS methods
os.chdir() # Change current working directory
os.access() # Can be use to detriment is a file exists or whether it is readable or writable.
os.listdir(".") # Returns file and directories in the path that is passed, excluding . and .. entries.   “.” is current directory
os.stat() # returns information about the directory such as mode, access time, and size.
os.mkdir() # To create directories.
os.mkdirs # make directories an intermediate directories.
os.remove() # To remove file or directories.
os.rename() # To rename files or directories.
os.walk() # Iterate over an entire directory tree retrieving the name of every file and directory in turn.

# More os.path methods
os.path.abspath() # Returns the absolute path of its argument.
os.path.split() # Returns a 2-tuple (path, filename)
os.path.basename()
os.path.dirname()
os.path.splitext() # Returns the file name and its extension.
os.path.join() # Takes any number of path strings & returns a single path using platform-specific path separator.
os.path.getsize() # Returns the size of the file name passed in bytes.
os.path.isfile() # Returns True if the path passed to it is that of a file and False otherwise.
os.path.isdir() # Returns True if the path passed to it is that of a directory and False otherwise.
os.path.exists() # returns True if path exists.
