a = True
b = False

print(not a) # False
print(a or b) # True since either have to be true
print(a and b) # False since both must be true

# 0, ‘ ‘, [ ], ( ), { }, None # All of these are False

print(5 == 5)# True
print(7 < 5)# False
print(type(True))# <class 'bool'>

# Boolean operators:
print(True and False)# False
print(True and True)# True
print(True or False)# True
print(False or False)# False

#Boolean examples (Typically used in a comparison operations)
a, b = 0, 1
x, y = 'zero', 'one'
print(x < y)# False
print(a < b)# True

if a < b and x < y:
    print('yes')
else:
    print('no')

#Bitwise arithmetic (using bitwise operator):
print(True & True)

