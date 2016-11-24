# Decorators can be thought of as functions which modify the functionality of another function.
'''
print('Globals:')
s = 'This is a global variable'
print(globals())
print(globals().keys())
print(globals()['s'])  # This is a global variable

print('\nLocals:')
def func():
    return locals()  # {}
print(func())

print('\nFunction are objects:')

def hello(name):
    return 'Hello ' + name

print(hello('Rafael'))  # hello Rafael
greet = hello
print(greet)  # <function hello at 0x7f6b01278bf8>
print(greet('Beto'))  # Hello Beto
del hello
#print(hello)  # NameError: name 'hello' is not defined
print(greet)  # <function hello at 0x7fed791e4950>

print('\nFunction within functions:\n')
print('functions names without () to assign, with () to execute')

def hello():
    print('hello function has been executed.')

    def greet():
        return '\tThis is inside the greet function.'

    def welcome():
        return '\tThis is inside the welcome function.'

    print(greet())
    print(welcome())
    print('Now we are back inside the hello function.')
hello()

print()

def hello(name='Beto'):
    print('hello function has been executed.')

    def greet():
        return '\tThis is inside the greet function.'

    def welcome():
        return '\tThis is inside the welcome function.'

    if name == 'Beto':
        return greet
    else:
        return welcome

x = hello()
print(x)  # <function hello.<locals>.greet at 0x7f06dfc2abf8>
print(x())  # This is inside the greet function. With () to execute the function.

print('\nFunctions as arguments\n')

def hello():
    return 'hello'

def other(func):
    print('other function stuff.')
    print(func())

print(other(hello))

print('\nDecorator manually:\n')

def new_decorator(func):
    def wrap_func():
        print('Code here before executing the func.')
        func()
        print('Code here after executing the func.')
    return wrap_func

def func_needs_decorator():
    print('This function needs a decorator!')

func_needs_decorator = new_decorator(func_needs_decorator)
print(func_needs_decorator())

print('\nDecorator with @ notation:\n')

'''

def new_decorator(func):
    def wrap_func():
        print('Code here before executing the func.')
        func()
        print('Code here after executing the func.')
    return wrap_func


@ new_decorator  # Execute new_decorator() before function_needs_decorator()
def func_needs_decorator():
    print('This function needs a decorator!')

func_needs_decorator()