# Make a tuple-based iterable object from items from each indexes

x = [1, 2, 3]
y = ['a', 'b', 'c']

for i in zip(x,y):
    print(i, end='')


print('Example 2, Select the largest from the index pair')

a = [1, 2, 3, 4, 5]
b = [2, 2, 10, 1, 1]

for i, j in zip(a, b):
    if i > j:
        print(i)
    else:
        print(j)

# Or

for i in map(lambda pair: max(pair), zip(a, b)):
    print(i, end=' ')

# OR

for pair in zip(a,b):
    print(max(pair))

# Dictionary

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5, 'f': 6}

print(d1.items())

for i in zip(d1.items(),d2.items()):
    print(i, end='')


