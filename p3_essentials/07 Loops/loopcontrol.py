#!/usr/bin/python3
# break.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('Continue example:')
    s = 'this is a string'
    for c in s:
        if c == 's':
            continue # skips this part of the iterator
        print(c, end='') # prints this i a string

    print('\nBreak example:')
    for c in s:
        if c == 's':
            break # break the loop after it finds the first s.
        print(c, end='') # prints thi

    print('\nelse example:')
    for c in s:
         print(c, end='')
    else:
        print(' no more letters')

    print('\nelse with while loop')
    i = 0
    while i < len(s):
        print(s[i], end='')
        i += 1
    else:
        print(' no more letters')







if __name__ == "__main__": main()
