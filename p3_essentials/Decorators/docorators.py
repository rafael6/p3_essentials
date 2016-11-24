'''
Apply @function_name to a function that will be passed to another function for
additional processing such as bound checking.
'''
'''
def outer(some_func):
    def inner():
        print("before some_func")
        ret = some_func() # 1
        return ret + 1
    return inner


def foo():
    return 1

decorated = outer(foo) # 2
print(decorated())
# or
foo = outer(foo)
print(foo())
'''

'''
def wrapper(func):
    def checker(a, b): #1
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret
    return checker

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coord: " + str(self.__dict__)
@wrapper
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)

@wrapper
def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)

one = Coordinate(100, 200)
two = Coordinate(300, 200)


#add = wrapper(add)  # substitute this with @wrapper above the decorated function
#sub = wrapper(sub)  # substitute this with @wrapper above the decorated function
print(sub(one, two))
'''

'''
Parameter logging function
Notice our inner function takes any arbitrary number and type of parameters at point #1
and passes them along as arguments to the wrapped function at point #2.
This allows us to wrap or decorate any function, no matter it's signature.
'''


def logger(func):
    def inner(*args, **kwargs): #1
        print("Arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs) #2
    return inner


@logger
def foo1(x, y=1):
    return x * y


@logger
def foo2():
    return 2

foo1(5, 4)
foo1(1)
foo2()