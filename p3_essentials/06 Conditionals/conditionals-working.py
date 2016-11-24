#!/usr/bin/python3

# 0, ‘ ‘, [ ], ( ), { }, None # All of these are False

def main():
    '''
    if, elif, and else statements evaluates to true or false.
    else is often used as the default
    only one of the suite is going to execute; the first match
    '''
    v = 'five'
    if v == 'one':
        print('v is one')
    elif v == 'two':
        print('v is two')
    elif v == 'three':
        print('v is three')
    else:
        print('v is something else!')

    print('------------------------------------------------------------------')
    print('Typical expressions')
    a, b = 1, 1
    if a < b:
        v = 'a is less than b'
    else:
        v = 'a is not less than b'
    print(v)

    print('Conditional expressions')
    v = 'a is less than b' if a < b else 'a is not less than b'
    print(v)

    print('------------------------------------------------------------------')
    print('More than one comparizon')
    x = 5
    y = 7
    z = 9

    if x < y < z:
        print(x, 'less than', y, 'and less than', z)

if __name__ == "__main__": main()
