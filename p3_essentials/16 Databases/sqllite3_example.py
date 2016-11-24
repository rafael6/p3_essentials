__author__ = 'rafael'

# A database is a collection of tables rows and columns.
# The columns are the fields and they must be specified by type such as text.
# import module
import sqlite3

# Create database connection for da named tutorial.db
conn = sqlite3.connect('tutorial.db')

# Create a cursor (pointer) where you can tell where to go, etc.
c = conn.cursor()


# Create table function
def create_table():
    # Normally you want caps for SQL commands
    # Create a table named example
    # Field Language, Version, and Skill fields
    # VARCHAR is any character any type any length
    # REAL are floats
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")


# Insert data function (Static)
def insert_data():
    # Insert this data into the previously specified fields
    c.execute("INSERT INTO example VALUES('Python', 2.7, 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', 2.3, 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Python', 2., 'Expert')")
    conn.commit()  # Commit the changes


def insert_dynamic_data():
    lang = input('What language? ')
    version = float(input('What version? '))
    skill = input('What skill level? ')
    c.execute("INSERT INTO example (Language, Version, Skill) VALUES (?, ?, ?)",
              (lang, version, skill))
    conn.commit()


# Read entire database
def read_from_database():
    # Select everything from the example table
    sql = "SELECT * FROM example"
    for row in c.execute(sql):
        # Print each row
        print(row)
        # Print first element of each road
        print(row[0])


# Matching a particular field value, static
def read_match_static():
    # Select rows where a particular field is matched
    sql = "SELECT * FROM example WHERE Skill == 'beginner'"
    for row in c.execute(sql):
        # Print matching row
        print(row)


# Matching a particular field value, dynamic
def read_match_dynamic():
    skill = input('What skill level? ')
    language = input('What language? ')
    # Matching multiple fields; you can also use OR logic
    sql = "SELECT * FROM example WHERE Skill = ? AND Language = ?"
    for row in c.execute(sql, [skill, language]):
        # Print matching row
        print(row)


# Limit the output
def limit_output():
    # Everything from example table, but limit the output to the first two rows
    sql = "SELECT * FROM example LIMIT 2"
    for row in c.execute(sql):
        # Print each row
        print(row)


def update_field():
    # Update the Skill field with value Beginner where is set to beginner
    sql = "UPDATE example SET Skill = 'Beginner' WHERE Skill = 'beginner'"
    c.execute(sql)
    sql = "SELECT * from example"
    for row in c.execute(sql):
        print(row)
    conn.commit()


# Delete a row where a matching field
def delete():
    sql = "DELETE FROM example WHERE Skill = 'Beginner'"
    c.execute(sql)
    conn.commit()


def read_all():
    sql = "SELECT * from example"
    for row in c.execute(sql):
        print(row)


# create_table()

# insert_data()

# insert_dynamic_data()

# read_from_database()

# read_match_static()

# read_match_dynamic()

# limit_output()

# update_field()

delete()

read_all()

conn.close()