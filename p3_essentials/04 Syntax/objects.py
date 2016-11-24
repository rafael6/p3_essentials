#!/usr/bin/python3
# shabang is needed when running programs from shell
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC


class Egg:
    def __init__(self, kind='fried'): # initializer with a default value for kind
        self.kind = kind # This is an object variable encapsulated in the object

    def whatkind(self):
        print('3.', self)
        return self.kind

def main():
    fried = Egg() # Create an Egg object using default parameter (ID is fried, type is Egg, value is 'fried'
    scrambled = Egg('scrambled') # Create an Egg object overriding default parameter
    print('1.', scrambled)
    print('2.', scrambled.kind) # self is scrambled.
    print(fried.whatkind())
    print('4.', scrambled.whatkind())# Envoke method whatkind


if __name__ == "__main__": main()
