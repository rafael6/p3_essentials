'''
Sqlite3 comes with python
'''
import sqlite3

def main():
    db = sqlite3.connect('test.db')  # Creates the database file
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
    db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into test (t1, i1) values (?, ?)', ('three', 3))
    db.execute('insert into test (t1, i1) values (?, ?)', ('four', 4))
    db.commit()  # Must commit after making changes to the database
    cursor = db.execute('select * from test order by t1')  # The cursor object is an iterator
    for row in cursor:
        print(row)

if __name__ == "__main__": main()



# sqllite3 row factory
def main():
    db = sqlite3.connect('test.db')  # Creates the database file
    db.row_factory = sqlite3.Row  # Allow you to specify how rows will be returned from the cursor
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
    db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into test (t1, i1) values (?, ?)', ('three', 3))
    db.execute('insert into test (t1, i1) values (?, ?)', ('four', 4))
    db.commit()  # Must commit after making changes to the database
    cursor = db.execute('select * from test order by t1')  # The cursor object is an iterator
    for row in cursor:
        print(dict(row)) # tuple(row), dict(row), list(row), row['t1'], row[i1]

if __name__ == "__main__": main()