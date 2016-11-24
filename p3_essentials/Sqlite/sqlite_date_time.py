import sqlite3
from datetime import date, datetime

# *** Date/Time as a string object
"""
db = sqlite3.connect(':memory:')

#Create table
with db:
    try:
        c = db.cursor()
        # If table closed --> sqlite3.ProgrammingError: Cannot operate on a closed database.
        c.execute('''CREATE TABLE example(id INTEGER PRIMARY KEY, created_at DATE)''')
    except sqlite3.ProgrammingError as e:
        print(e)

# Insert a date object into the database
with db:
    try:
        today = date.today()
        c.execute('''INSERT INTO example(created_at) VALUES(?)''', (today,))
    except Exception as e:  # Need to fix
        raise e

# Retrieve the inserted object
with db:
    try:
        c.execute('''SELECT created_at FROM example''')
        row = c.fetchone()
        # The datatype is <class 'str'>
        print('The date is {0} and the datatype is {1}'.format(row[0], type(row[0])))
    except Exception as e:  # Need to fix
        raise e

db.close()
"""

# ***Date/Time as a date.time object
"""
db = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
c = db.cursor()

with db:
    try:
        c.execute('''CREATE TABLE example(id INTEGER PRIMARY KEY, created_at timestamp)''')
    except sqlite3.ProgrammingError as e:
        print(e)

# Insert a datetime object
with db:
    try:
        now = datetime.now()
        c.execute('''INSERT INTO example(created_at) VALUES(?)''', (now,))
    except sqlite3.ProgrammingError as e:
        print(e)

# Retrieve the inserted object
with db:
    try:
        c.execute('''SELECT created_at FROM example''')
        row = c.fetchone()
        # The datatype is <class 'datetime.datetime'>
        print('The date is {0} and the datatype is {1}'.format(row[0], type(row[0])))
    except sqlite3.ProgrammingError as e:
        print(e)

db.close()
"""

