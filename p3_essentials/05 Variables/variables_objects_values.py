# Everything in python is an object
# Every object has an ID, type, and value
#Object are mutable or immutable

# immutable objects may look like it's value change, but it is not.
# Distinction is visible using id() method
# Ex. integers are immutable:

x = 42
print('x = 42; the value of x is: ', x)
print('x is type: ', type(x))
print('x id is: ', id(x))

print('----------------------------------------------------------------------')
print('x = 43; change the variable to refer to a different object')
x = 43
print('The value of x is now: ', x)
print('x id is now: ', id(x))

print('----------------------------------------------------------------------')
print('x = 42; change the variable to refer back to the original object')
x = 42
print('The value of x is back to: ', x)
print('x id is back to: ', id(x))

print('\nWe simply change the variable to refer to a different object.')

print('----------------------------------------------------------------------')
print('y = 42; Assign another reference to the same object')
print('x == y compares the value, x is y compares the ID.')
y = 42
print('x and y reference the same object', id(x), id(y))
print(x == y)  # compares the values
print(x is y)  # compares the ID

print('----------------------------------------------------------------------')
print('')
d = dict(x=42)
print(type(d))
print(d)
print(id(d))
e = dict(x=42)
print(type(e))
print('Mutable objects such as dicts have different IDs even with the same value', id(e), id(d))
print('They are equal in value:', d == e)
print('But not the same object:', d is e)


print('----------------------------------------------------------------------')
print('Immutable are: numbers, strings, tuples')
print('''Immutable means if you change its  value, it becomes a different object
>>> z = 42
>>> id(z)
10456352
>>> z = z + 1
>>> id(z)
10456384
''')
print('Mutable objects are: lists, dictionaries, and other objects depending upon implementation')