#!/usr/bin/python3


def main():
    fh = open('lines.txt') # fh is the file object
    for line in fh.readlines(): # The readlines method is the iterator
        print(line, end='')

    print('---------------------------ENUMERATE 1-----------------------------')
    print('Enumerate example 1:')
    fh = open('lines.txt')
    for index, line in enumerate(fh.readlines()):
        print(index, line, end='')

    print('---------------------------ENUMERATE 2------------------------------')
    print('Enumerate example 2:')
    s = 'this is a string'
    for i, c in enumerate(s):
        print(i, c)

    print('---------------------------ENUMERATE 3----------------------------')
    print('Enumerate example 3:')
    s = 'this is a string'
    for i, c in enumerate(s):
        if c == 's':
            print('Index {} is an s in the string'.format(i))

    print('---------------------------- RANGE--------------------------------')
    print('range() example 4:')
    # range() method creates a list, but when used this way is faster than pre-define the list.
    for i in range(1, 5):
        print(i)

    print('----------------------DICTIONARY K&V------------------------------')
    d = {'one': 1, 'two': 2, 'three': 3}
    for k, v in d.items():
        print(k, v)

    print('----------------------DICTIONARY K------------------------------')
    d = {'one': 1, 'two': 2, 'three': 3}
    for k in d:
        print(k)

    print('----------------------DICTIONARY K------------------------------')
    d = {'one': 1, 'two': 2, 'three': 3}
    for v in d.values():
        print(v)

if __name__ == "__main__": main()
