'''
strings are objects; so you can do things such as:
'this is a string'.upper()

You should use the join() method when joining two strings not + operator
'''

def main():
    s = 'this is a  string'
    print(s.capitalize())  # Capitalize the first letter.
    print(s.title())  # Capitalize the first letter of each word.
    print(s.upper())  # Capitalize the entire string; there is a lower() method which lowers the entire string.
    print(s.swapcase())  # Swap the case of each letter Caps <-> Lower.
    print(s.find('is'))  # Returns the first position where 'is' was found.
    print(s.replace('this', 'that'))  # Replaces 'this' with 'that'
    print(s.strip())  # strips a particular sequence of characters from both the end of the string & the
    # beginning of the string. Default is whitespace. rstrip() method removes just end of the strip.
    # Ex. rstrip('\n') to remove just the new line from the end.
    print(s.isalnum())  # checks if the string has only alphanumeric characters in it; False since there is whitespace.
    print(s.isalpha())  # Checks just for alpha characters. So that would be the letters a-z
    print(s.isdigit())  # Check if the string is just digits
    print(s.isprintable())  # Check if all the characters in the string are printable

    #strings are immutable; therefore, the methods below return a different object.
    # s and new_string are different objects
    new_string = s.upper()
    print(id(s))
    print(id(new_string))

    print('\n')

    s = 'This is a string'
    print(s.split())  # Default is to split at white space. Returns a list ['This', 'is', 'a', 'string']
    print(s.split('i')) # Remove "i" and split at "i". Returns ['Th', 's ', 's a str', 'ng']

    print('\n')
    s = ['This', 'is', 'a', 'string']
    print(' '.join(s))  # Returns  This is a string
    print(':'.join(s))  # Returns  This:is:a:string
    print(', '.join(s))  # Returns  TThis, is, a, string

    print('\n')
    s = 'This is a string'
    new = s.center(80) # will center in an 80 character width
    print(new)
    print(len(new)) # 80




if __name__ == "__main__":
    main()
