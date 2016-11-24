'''
A generator object is an object that can be used in the context of an iterable
'''

class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1:
            raise TypeError('Requires at least one argument')
        elif numargs == 1:
            self.start = 0
            self.stop = args[0] # or self.stop, = args   since it is a tuple needs the comma for a single item.
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError('Expected at must, but {} were given'.format(numargs))

    def __iter__(self):# makes the object an iterable object
        i = self.start
        while i <= self.stop:
            yield i # while condition True, yield i. next time loop is called; it start below. It makes it a generator
            i += self.step # start of every iteration after the first one

def main():
    # start at 1, stop at 25, steps of 5
    # you don't have to use inclusive_range.iter this class has an an __iter__ method
    for i in inclusive_range(5, 25, 5):
        print(i, end = ' ')

if __name__ == "__main__":
    main()
