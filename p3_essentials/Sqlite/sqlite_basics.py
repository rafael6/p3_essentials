#!/usr/bin/python3

import sqlite3


# ***Connect to db if doesn't exist create db
db = sqlite3.connect('mydb')

# ***Close db connection
#db.close()

# ***Create table named users
"""
#Create table
# Create a cursor object and use its execute method to execute operations
# If table closed --> sqlite3.ProgrammingError: Cannot operate on a closed database.
cursor = db.cursor()
# Create a table named users
# If you try to create again --> sqlite3.OperationalError: table users already exists
# if table closed --> sqlite3.ProgrammingError: Cannot operate on a closed database.
cursor.execute('''
    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                       phone TEXT, email TEXT unique, password TEXT )
''')
db.commit()
"""

# ***Delete table named users
"""
# Delate table
cursor = db.cursor()
# If table doesn't exists --> sqlite3.OperationalError: no such table: users
cursor.execute('''DROP TABLE users''')
db.commit()
"""


# ***Insert data into table (db)users
"""
cursor = db.cursor()

name1 = 'Andres'
phone1 ='1234567899'
email1 = 'user@example.com'
password1 = '12345'

name2 = 'John'
phone2 ='3214567899'
email2 = 'john@somewhwre.com'
password2 = 'abcdf'

# Insert user 1
# If a field such as password doen't exists --> sqlite3.OperationalError: table users has no column named pasword
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name1, phone1, email1, password1))
print('First user inserted')
# Insert user2
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name2, phone2, email2, password2))
print('Second user inserted')
# To print the id of the row you just entered
id = cursor.lastrowid
print('Last row id: {}'.format(id))
db.commit()
"""

# *** Fetch options for db users
"""
cursor = db.cursor()
# if db closed --> sqlite3.ProgrammingError: Cannot operate on a closed database.
cursor.execute('''SELECT name, email, phone FROM users''')
print('Point 1:')
# fetch one row
user1 = cursor.fetchone() #retrieve the first row
print(user1[0]) #Print the first column retrieved(user's name)
print('Point 2:')
# Fetch the entire table; not in this example since we already fetched the first row
all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] returns name column, row[1] returns email column, row[2] phone column
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

print('Point 3:')
# The cursor object works as an iterator, invoking fetchall() automatically:
cursor.execute('''SELECT name, email, phone FROM users''')
for row in cursor:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

# To retrieve data with conditions, use again the "?" placeholder:
print('Point4')
user_id = 1
cursor.execute('''SELECT name, email, phone FROM users WHERE id=?''', (user_id,))
user = cursor.fetchone()
print(user)
"""

# ***Update and delete data
"""

cursor = db.cursor()

# Update user with id 1
newphone = '2222222222'
userid = 1
cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''',
 (newphone, userid))

# Delete user with id 2
delete_userid = 2
cursor.execute('''DELETE FROM users WHERE id = ? ''', (delete_userid,))

db.commit()

# if db closed --> sqlite3.ProgrammingError: Cannot operate on a closed database.
cursor.execute('''SELECT name, email, phone FROM users''')
# Fetch the entire table; not in this example since we already fetched the first row
all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] returns name column, row[1] returns email column, row[2] phone column
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

# Or rollback; need clarification
#cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''',(newphone, userid))
# The user's phone is not updated
#db.rollback()
"""

# ***Context manager to automatically commit or rollback transactions (with)
"""
cursor = db.cursor()

name1 = 'Andres'
phone1 ='1234567899'
email1 = 'user@example.com'
password1 = '12345'

name2 = 'John'
phone2 ='3214567899'
email2 = 'john@somewhwre.com'
password2 = 'abcdf'

try:
    with db:
        # Insert user 1
        # If a field such as password doen't exists --> sqlite3.OperationalError: table users has no column named pasword
        # If the table doesn't exists --> sqlite3.OperationalError: no such table: users
        cursor.execute('''INSERT INTO users(name, phone, email, password)
                          VALUES(?,?,?,?)''', (name1, phone1, email1, password1))
        print('First user inserted')
        # Insert user2
        cursor.execute('''INSERT INTO users(name, phone, email, password)
                          VALUES(?,?,?,?)''', (name2, phone2, email2, password2))
        print('Second user inserted')
        # To print the id of the row you just entered
        id = cursor.lastrowid
        print('Last row id: {}'.format(id))
except sqlite3.IntegrityError:
    print('Record already exists')
finally:
    db.close()
"""

# ***Sqlite3.Row used to access the columns of a query by name instead of index.
"""
db = sqlite3.connect('mydb')
db.row_factory = sqlite3.Row
cursor = db.cursor()
try:
    with db:
        # if db closed --> sqlite3.ProgrammingError: Cannot operate on a closed database.
        cursor.execute('''SELECT name, email, phone FROM users''')
        for row in cursor:
            # row['name'] returns the name column in the query, row['email'] returns email column.
            print('{0} : {1}, {2}'.format(row['name'], row['email'], row['phone']))
except Exception as e:  # Need to fix
    raise e
finally:
    db.close()
"""