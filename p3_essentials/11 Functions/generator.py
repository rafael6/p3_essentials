"""
A generator is function producing a series of values.

Regular functions only get one chance to return results, and thus must return
all results at once.

A generator is a function that returns an iterator object

because we're using yield instead of return, the next time the function is
called execution will continue right after the yield statement.
So the next thing that will happen is it will get incremented by step and then
the loop will be tested again.

what makes the yield different than return is that as the function gets called over
and over again, each time execution begins right after the yield and continues as
if the function were running continually.

After one pass the generator object is empty; therefore, if you need to give it a
pass more than once use an iterator instead.


"""

print('Iterator example')

class BeyonceIterable(object):
    def __iter__(self):
        """
        The iterable interface: return an iterator from __iter__().

        Every generator is an iterator implicitly (but not vice versa!),
        so implementing `__iter__` as a generator is the easiest way
        to create streamed iterables.

        """
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if i % 2 == 0:
              yield i# uses yield => __iter__ is a generator

iterable = BeyonceIterable()

for val in iterable:  # iterator created here
    print(val)

for val in iterable:  # another iterator created here
    print(val)


print('\nEven number example:\n')

generator = (i for i in [1, 2, 3, 4, 5, 6, 7, 8, 9] if i %2 == 0)
for i in generator:
    print(i)

print('xxxxxxx')
# Belo will not generate results becouse the generator object is empty
def gen(list):
    for i in list:
        if i % 2 == 0:
            yield i

for i in gen([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print(i)

print('\nFibonacci example:')


def get_fibonacci(n):
    a = 0
    b = 1
    for i in n:
        yield a
        a, b = b, a+b

for num in get_fibonacci(range(10)):
    print(num)


print('\nPrime numbers example:')


def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def primes(n = 1):
   while(True):
       if isprime(n):
           yield n # yield is like return, but it return an iterator object the for loop below can use.
       n += 1

for n in primes():
    if n > 10: break
    print(n)

print('\nnext() method:')


def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
#print(next(g))  # StopIteration error

"""
def main():
    for i in inclusive_range(1, 25, 1):
        print(i, end = ' ')

def inclusive_range(start, stop, step):
    i = start # 1. i = 1
    while i <= stop: # 25 or less
        yield i # 1. i = 1
        i += step # This is the beginning of the next iteration and i = 2 now.

if __name__ == "__main__": main()
"""

print('\n')
"""

def main():
    for i in inclusive_range(1, 25, 1):
        print(i, end = ' ')

def inclusive_range(*args):
    numargs = len(args)
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
"""