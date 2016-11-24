print('Booleans are mutable; therefore two references can point to the same object')
print('----------------------------------------------------------------------')
a, b = 0, 1
print('Returns a boolean value of:', a == b)
print('Returns a boolean value of:', a < b)
print('Returns a boolean value of:', a > b)

print('----------------------------------------------------------------------')
print('Assign True of False to variables')
a = True
print(a)
print('The type for booleans is:', type(a))
b = True
print('They are mutable:',  a is b)

