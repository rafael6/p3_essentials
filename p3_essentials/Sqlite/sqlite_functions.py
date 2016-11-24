
__author__ = 'rafael'

import sqlite3

db = ''


def db_connect(db_name):
    """Creates a connection that represents the database.
    :param db_name: name of database object
    :return:
    """
    global db
    """Connect to db. If it doesn't exist create the db
    """
    db = sqlite3.connect(db_name)
    # return db


def db_delete():
    """Deletes table ip_elements."""
    with db:
        try:
            cursor = db.cursor()
            cursor.execute('''DROP TABLE ip_elements''')
        except sqlite3.OperationalError as e:
            print(e)
        else:
            print('Table ip_element deleted')


def sql(sql):
    """Executes an SQL statement.
    """
    # db = db_connect('pito')
    with db:
        try:
            cursor = db.cursor()
            cursor.execute(sql)
        except sqlite3.ProgrammingError as e:
            print(e)
        except sqlite3.OperationalError as e:
            print(e)
        else:
            print('Sql action completed')


def insert(timestamp, element, element_type, dns, ping, port, url):
    """
    Insert a record into ip_elements table.
    :param element: Element's host name or IP
    :param dns_status: DNS resolution for the element's host name; optional
    :param port_status: Port status
    :param url_status: URL status; optional
    :return:
    """
    sql = '''INSERT INTO ip_elements(date_time, ip_element, element_type,
    dns_status, ping_status, port_status, url_status)VALUES(?,?,?,?,?,?,?)'''

    with db:
        try:
            cursor = db.cursor()
            cursor.execute(sql, (timestamp, element, element_type, dns, ping, port, url))
        except sqlite3.OperationalError as e:
            print(e)
        else:
            print('Inserted {},{},{},{},{},{},{}.'.format(
                timestamp, element, element_type, dns, ping, port, url))


def fetch_all():
    """
    Fetch all the records and fields in the table
    :return:
    """
    sql = '''SELECT date_time, ip_element, element_type, dns_status, ping_status,
    port_status, url_status FROM ip_elements'''
    with db:
        try:
            cursor = db.cursor()
            cursor.execute(sql)
        except sqlite3.ProgrammingError as e:
            print(e)
        else:
            for row in cursor:
                print('Datetime:{}, Element: {}, Type: {}, DNS Status: {},'
                      'Ping Status: {}, Port Status: {}, URL Status: {}'
                      .format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))


def main():
    db_connect('pito')

    db_delete()

    # Schema definition
    table_sql = '''
    CREATE TABLE ip_elements(id INTEGER PRIMARY KEY, date_time DATE,
    ip_element TEXT, element_type TEXT, dns_status TEXT, ping_status TEXT,
    port_status TEXT, url_status TEXT )'''

    sql(table_sql)

    insert('today', 'google.com', 'vip', 'dns_ok', 'ping_ok', 'port_ok', 'url_ok')

    fetch_all()

if __name__ == "__main__":
    main()