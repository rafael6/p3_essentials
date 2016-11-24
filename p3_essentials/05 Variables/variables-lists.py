#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('------------------------------------------------------------------')
    print('This is a tuple and it is immutable')
    x = (1, 2, 3)
    print(type(x), x)
    print('------------------------------------------------------------------')
    print('This is a list and it is mutable')
    x = [1, 2, 3]
    print(type(x), x)
    x.append(5)
    print(x)
    x.insert(0, 7)
    print(x)
    print('------------------------------------------------------------------')
    print('This is a string and it is mutable')
    x = 'string'
    print(type(x), x)
    print(x[2])
    print(x[2:4])
    print('------------------------------------------------------------------')
    print('Sequence are iterables')
    x = 'string'
    for i in x:
        print(i, end='')
    x = (1, 2, 3)
    for i in x:
        print(i)



if __name__ == "__main__": main()
