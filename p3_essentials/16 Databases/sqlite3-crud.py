'''
CRUD = create, retrieve, update and delete.
'''

import sqlite3

# insert(db, dict(t1 = 'one', i1 = 1))
def insert(db, row):  # row is: {'i1': 1, 't1': 'one'}
    db.execute('insert into test (t1, i1) values (?, ?)', (row['t1'], row['i1']))  # ('one', 1)
    db.commit()

# print(dict(retrieve(db, 'one')), dict(retrieve(db, 'two')))
def retrieve(db, t1):  # t1 is 'one', 'two'
    cursor = db.execute('select * from test where t1 = ?', (t1,)) # ('one'), ('two')
    return cursor.fetchone() # {'i1': 1, 't1': 'one'} {'i1': 2, 't1': 'two'}

# update(db, dict(t1 = 'one', i1 = 101))
def update(db, row):  # row is {'t1': 'one', 'i1': 101}
    db.execute('update test set i1 = ? where t1 = ?', (row['i1'], row['t1']))  # (101, 'one')
    db.commit()

# delete(db, 'one')
def delete(db, t1):  # t1 is 'one'
    db.execute('delete from test where t1 = ?', (t1,))  # ('one',)
    db.commit()

#  disp_rows(db)
def disp_rows(db): # db is an sqlite3 object
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print('  {}: {}'.format(row['t1'], row['i1']))

def main():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row
    print('Create table test')
    db.execute('drop table if exists test')
    db.execute('create table test ( t1 text, i1 int )')

    print('Create rows')
    insert(db, dict(t1 = 'one', i1 = 1))
    insert(db, dict(t1 = 'two', i1 = 2))
    insert(db, dict(t1 = 'three', i1 = 3))
    insert(db, dict(t1 = 'four', i1 = 4))
    disp_rows(db)

    print('Retrieve rows')
    print(dict(retrieve(db, 'one')), dict(retrieve(db, 'two')))

    print('Update rows')
    update(db, dict(t1 = 'one', i1 = 101))
    update(db, dict(t1 = 'three', i1 = 103))
    disp_rows(db)

    print('Delete rows')
    delete(db, 'one')
    delete(db, 'three')
    disp_rows(db)

if __name__ == "__main__": main()
