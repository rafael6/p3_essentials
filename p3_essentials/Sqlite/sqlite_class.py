__author__ = 'rafael'

import sqlite3


class database:
    """Usage: db = database(filename = 'test.db', table = 'test')
        self.filename: is the name of the .db file
        self.table: the name of the db schema
    """
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')  # filename is a dict key
        self.table = kwargs.get('table', 'test') # 'table' is dict key, test is a default name

    # Executes a sql statement; _db is an internal instance of database named filename
    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()

    def insert(self, row):
        self._db.execute('''INSERT INTO {} (date_time, ip_element, element_type,
        dns_status, ping_status, port_status, url_status) VALUES (?, ?, ?, ?, ?, ?, ?)'''.
                         format(self._table), (row['date_time'], row['ip_element'],
                                               row['element_type'], row['dns_status'],
                                               row['ping_status'], row['port_status'],
                                               row['url_status']))
        self._db.commit()

    def retrieve_element(self, key):
        cursor = self._db.execute('select * from {} where ip_element = ?'.
                                  format(self._table), (key,))
        return dict(cursor.fetchone())

    def retrieve_all(self, key):
        #cursor = self._db.cursor()
        #cursor.execute('select * from {} where ip_element = ? order by date_time'.format(self._table), (key,))
        cursor = self._db.execute('select * from {} where ip_element = ? order by date_time'.format(self._table), (key,))
        for row in cursor:
            print(dict(row))

    def print_all(self):
        #cursor = self._db.cursor()
        #cursor.execute('select * from {} where ip_element = ? order by date_time'.format(self._table), (key,))
        cursor = self._db.execute('select * from {} order by date_time'.format(self._table))
        for row in cursor:
            print(dict(row))

    def delete(self, key):
        self._db.execute('delete from {} where ip_element = ?'.format(self._table), (key,))
        self._db.commit()

    def disp_rows(self):
        cursor = self._db.execute('select * from {} order by date_time'.
                                  format(self._table))
        for row in cursor:
            print('{}, {}, {}, {}, {}, {}, {}'.format(row['date_time'],
                                                      row['ip_element'],
                                                      row['element_type'],
                                                      row['dns_status'],
                                                      row['ping_status'],
                                                      row['port_status'],
                                                      row['url_status']))


    def disp_all_filter(self, key):
        cursor = self._db.execute('select * from {} where ip_element = ?'.
                                  format(self._table), (key,))
        for row in cursor:
            print('{}, {}, {}, {}, {}, {}, {}'.format(row['date_time'],
                                                      row['ip_element'],
                                                      row['element_type'],
                                                      row['dns_status'],
                                                      row['ping_status'],
                                                      row['port_status'],
                                                      row['url_status']))

    def __iter__(self):
       cursor = self._db.execute('select * from {} order by date_time'.format(self._table))
       for row in cursor:
           yield dict(row)

    # Assign filename to _filename
    @property
    def filename(self):
        return self._filename

    # Set filename to _filename
    # self.filename = kwargs.get('filename')
    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self):
        self.close()


    # access: self.table    return: self._table
    # not accessed; Needed for the table.setter and table.deleter to exists
    @property
    def table(self):
        return self._table # Needed for the table.setter and table.deleter

    # access self.table = 'test'   assign: 'test' to self._table
    # self.table = kwargs.get('table', 'test')
    @table.setter
    def table(self, t):
        self._table = t

    @table.deleter
    def table(self):
        self._table = 'test'


def main():

    db = database(filename='test.db', table='ip_elements')

    print('Create table test')

    db.sql_do('drop table if exists ip_elements')

    schema = '''
    CREATE TABLE ip_elements (id INTEGER PRIMARY KEY, date_time DATE,
    ip_element TEXT, element_type TEXT, dns_status TEXT, ping_status TEXT,
    port_status TEXT, url_status TEXT )'''
    db.sql_do(schema)

    # Create rows
    print('Create rows')
    record = dict(date_time='2015-09-06 23:58:48.579970', ip_element='cnn.com',
                  element_type='vip', dns_status='1.1.1.1', ping_status='no loss',
                  port_status='open', url_status='200 ok')
    db.insert(record)

    record = dict(date_time='2015-04-06 23:58:48.777770', ip_element='cnn.com',
                  element_type='vip', dns_status='1.1.1.1', ping_status='no loss',
                  port_status='open', url_status='200 ok')
    db.insert(record)

    record = dict(date_time='2015-10-07 12:07:48.667757', ip_element='yahoo.com',
                  element_type='vip', dns_status='1.1.1.1', ping_status='no loss',
                  port_status='open', url_status='200 ok')
    db.insert(record)

    record = dict(date_time='2015-10-07 12:07:48.667755', ip_element='google.com',
                  element_type='vip', dns_status='1.1.1.1', ping_status='no loss',
                  port_status='open', url_status='200 ok')
    db.insert(record)

    # Prints every row; ordered by date/time; no filter
    #for row in db:  # need iter
        #print(row)

    # Prints every row that contains a given value; ordered by ID; no dic
    #print('Test1...')
    #db.disp_all_filter('cnn.com')

    # Retrieve first element with cnn.com
    print('Retrieve first row with a given value')
    print(db.retrieve_element('cnn.com'))

    ######### Retrieve all element with cnn.com
    print('Retrieve all rows with a given value; ordered by date/time')
    db.retrieve_all('cnn.com')

    ######## Retrive all oordered by date/time
    print('Retrieve all rows; ordered by date/time')
    db.print_all()

    # Deletes
    #print('Delete every row with a given value')
    db.delete('cnn.com')

    #nPrints every row; ordered by date/time; no fileter
    print('All ordered by date/time')
    for row in db:  # need iter
        print(row)

    #print('Display all the rows in order by date/time')
    #db.disp_rows()


if __name__ == "__main__":
    main()