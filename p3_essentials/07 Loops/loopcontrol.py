#!/usr/bin/python3

# Continue is to skip an item in the iterator and contine with the loop.
# Break is to break out of the loop.

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
    # Primary use of else statement is to find an item
    # The else statement in this example only execute if the entire list is exasted
    my_list = [1, 2, 3, 4, 5]

    for i in my_list:
        if i == 3:
            print("Item found!")
            break
        print(i)
    else:
        print("Item not found!")

# Another example
    i = 0
    while i < len(s):
        print(s[i], end='')
        i += 1
    else:
        print(' no more letters')







if __name__ == "__main__": main()
