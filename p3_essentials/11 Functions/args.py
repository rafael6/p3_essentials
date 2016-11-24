
def main():
    testfunc(1, 2, 3, 50, 51, 52)

# *args is positional arguments assigned to variable args in a tuple form
def testfunc(this, that, other, *args):
    print(this, that, other, args)  # returns 1 2 3 (50, 51, 52)

if __name__ == "__main__":
    main()


print('\n')
# Example use for args
def main():
    for i in inclusive_range(1, 25, 1):
        print(i, end = ' ')

def inclusive_range(*args):
    numargs = len(args) # Needed to control the number of arguments and raise exceptions as needed
    if numargs < 1: raise TypeError('Requires at least one argument.')
    elif numargs == 1:
        start = 0
        stop = args[0]
        step = 1
    elif numargs == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif numargs == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        raise ValueError('Function expects at most 3 arguments, but received {}'.format(numargs))
    i = start # 1. i = 1
    while i <= stop: # 25 or less
        yield i # 1. i = 1
        i += step # This is the beginning of the next iteration and i = 2 now.

if __name__ == "__main__": main()