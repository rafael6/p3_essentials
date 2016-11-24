#!/usr/bin/python3

# 0, ‘ ‘, [ ], ( ), { }, None # All of these are False

# Conditionals:
def main():
    a, b = 1, 1
    if a < b:
        print('a is less than b')
    elif a > b:
        print('a is greater than b')
    else:
        print('a is equal to b')

if __name__ == "__main__": main()


# Another conditionals example using format method:
a, b = 5, 1
if a < b:
    print('a ({}) is less than b ({})'.format(a, b))
else:
    print('a ({}) is not less than b ({})'.format(a, b))



# Conditional expressions:
def main():
    a, b = 0, 1
    s = 'a less than b' if a < b else 'a not less than b' # This is a conditional expression.
    print(s)


if __name__ == "__main__": main()