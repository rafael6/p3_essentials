
'''
Tuples are immutable; no t[0] = 5
'''

# Classic use of tuples
def func():
    return 'yes', 'no'

y, n = func()
print(y)
print(n)

# More on tuples
t = 1,2,3,4,5 # The comma makes it a tuple
print(type(t))
print(t[0]) #  First item
print(t[-1]) # last item
print(min(t))
print(max(t))

print('\n')

t1 = 1, # This is how to define a single item tuple. Or (1,)
print(t1)
print(type(t1))# is a tuple
t1 = (1) # This is not a single item tuple! Is an integer.
print(t1)
print(type(t1))# Is an integer


print('\n')

# List are mutable
l = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l)
print(type(l))

# Change a value of an item
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[0]=7  # assign 7 to position 0
print(l)

# Insert an item in a particular place
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l.insert(5, 7)  # in position 5 insert integer 7
print(l)

# Remove an item in a particular place
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l.remove(7)  # Remove the first 7 from the list
print(l)

# Get the index of a particular item
l = ['a', 'b', 'c']
print(l.index('c'))  # Prints the index for item with value 9.

# Get the number of instances of a particular item
l = ['a', 'b', 'c', 'c', 'c']
print(l.count('c'))

# Sort a list
l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sorted(l))
l = ['zack', 'jack', 'ham']
print(sorted(l))

# Reverse a list
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l.reverse()
print(l)

