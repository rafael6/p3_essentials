'''
List and tuples are ordered data type
'''

# Initialize a tuple:

t = tuple(range(10)) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t)

print()

print(5 in t)  # True
print(15 in t)  # False
print(15 not in t)  # True

print()

print(len(t))  # 10
print(t[3])  # 3
print(t.count(3)) # Returns how many times item 3 is in the tuple; 1 in this example.
print(t.index(5)) # Returns the index of item 5
print()

for i in t: print(i, end='')  # 0123456789

print('\n')

# You can apply the same methods above to lists!
l = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l)

print()

#Lists are mutable
l[5] = 7
print(l)  # [0, 1, 2, 3, 4, 7, 6, 7, 8, 9]

l.append(100)  # [0, 1, 2, 3, 4, 7, 6, 7, 8, 9, 100]
print(l)

l.extend(range(10))  # [0, 1, 2, 3, 4, 7, 6, 7, 8, 9, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l)

l.insert(0, 7)  # Insert 7 in index 0; [7, 0, 1, 2, 3, 4, 7, 6, 7, 8, 9, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l)

l.remove(7)
print(l)  # Removes the first item with value 7; [0, 1, 2, 3, 4, 7, 6, 7, 8, 9, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


del l[10]  # Deletes the item in index 10; [0, 1, 2, 3, 4, 7, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l)

print(l.pop())  # Removes and returns the lat item in the list; 9
print(l)  # [0, 1, 2, 3, 4, 7, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8]

print(l.pop(0))  # Removes from the beginning and return value; 0
print(l)  # [1, 2, 3, 4, 7, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8]

