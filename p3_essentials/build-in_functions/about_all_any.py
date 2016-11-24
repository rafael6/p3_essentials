'''
allow us to convienently check for boolean matching in an iterable.
all() will return True if all elements in an iterable are True.
'''

lst = [True, True, False, False]

# Returns False since not all are True
print(all(lst))

# Returns True if any is True
print(any(lst))


