#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('Raw string:')
    s = r'This is a\nraw string!'
    print(s)
    print('-------------------------------------------------------------------')

    print('This is an example of the format method:')
    n = 42
    s = 'This is a {} string!'.format(n)
    print(s)
    print('-------------------------------------------------------------------')

    print('This is an example of the format method:')
    s = '''\
This is a way to
print multiple lines
the slash is to avoid
a line space before the string.
'''
    print(s)


if __name__ == "__main__": main()
