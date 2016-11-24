import sqlite3 #Import the SQLite3 module
import hashlib

'''
Sometimes we need to use our own functions in a statement, specially when we are
inserting data in order to accomplish some specific task. A good example of this
is when we are storing passwords in the database and we need to encrypt those passwords:

The create_function takes 3 parameters: name (the name used to call the function
inside the statement), the number of parameters the function expects
(1 parameter in this case) and a callable object (the function itself).
To use our registered function, we called it using encrypt() in the statement.
'''
def encrypt_password(password):
    # Do not use this algorithm in a real environment
    encrypted_pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
    return encrypted_pass

db = sqlite3.connect(':memory:')
# Register the function
db.create_function('encrypt', 1, encrypt_password)
c = db.cursor()
c.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT, password TEXT)''')
user = ('johndoe@example.com', '12345678')
c.execute('''INSERT INTO users(email, password) VALUES (?,encrypt(?))''', user)