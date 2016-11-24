'''
They are unordered
Key must be unique

Coomon methods: d.keys(), d.values, d.items()
'''

# Classic build
d = {'one': 1, 'two': 2, 'three': 3}
print(d)

# Retriving values
print(d['one']) # Retrive a value; KeyError if key does’t exist.
print(d.get('one')) # Retrive a value; no exception; returns none if key doesn’t exist.
print(d.get('five', 'Not found'))# same as above, but with a default value

# Update the value for a particular key
d = {'one': 1, 'two': 2, 'three': 3}
d['one'] = 4
print(d)

# To add a key/value pair to dictionary
d = {'one': 1, 'two': 2, 'three': 3}
d['four'] = 4
print(d)

# To delete a key/value pair to dictionary
d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
del d['four']
print(d)

# To clear a dictionary (Delete all Ks and Vs, but retain the variable)
d.clear()

# Containers as value
d = {'sebee':[1, 10], 'beto':[2, 20], 'raf':[3, 30]}
print(d['beto'][1])


# Using a constructor
d = dict(one=1, two=2, three=3)
print(d)

# You can initialize a dictionary from another dictionary:
d1 = dict(four=4, five=5, six=6)
d = dict(one=1, two=2, three=3, **d1)
print(d) #  {'one': 1, 'four': 4, 'six': 6, 'three': 3, 'five': 5, 'two': 2}

print()

# Print all the keys:
print(d.keys())  # Returns a list with all key
for k in d: print(k)  # Iterate over each key
print()
# use this form when mutating the since a.keys() makes a copy of all the keys
# and stores them in a list.
for k in d.keys(): print(k)

print()

# Print all keys in order
for k in sorted(d): print(k)

print()

# Print all values:
print(d.values()) # Returns a list containing all the values.

for v in d.values(): print(v)  # Iterate over each value.

for v in sorted(d.values()): print(v)  # Print all values in order

print()

#Print key and values:
for k, v in d.items(): print(k, v)

for k, v in sorted(d.items()): print(k, v)  # Print key and value sorted by key

print()

# Methods:
d = {'one': 1, 'two': 2, 'three': 3}
print('two' in d)  # True

print(d.items())  # Returns tuples each containing a key and a value

print(d.pop('three'))  # Returns and remove the specify element; 3
print(d)

# Examples:

# Dictionary as a switch with default value:
choices = dict(
    one='first',
    two='second',
    three='third',
    four='fourth',
    five='fifth'
)
v = 'three'
print(choices.get(v, 'Not found'))

# How to shallow copy a dictionary
d = {'one': 1, 'two': 2, 'three': 3}
d1 = dict.copy(d)  # or d1 = dict(d).  d and d1 reference the same object in memory

# How to deep copy
import copy
d1 = copy.deepcopy(d) # d and d1 are now refer to different objects in memory.

# How to create a dictionary from two lists)
# izip supposed to be better than zip, but I can’t find a reference to it.
names = ['ray', 'rachel', 'matthew']
colors = ['blue', 'red', 'yellow']
d = dict(zip(names, colors))  # {'rachel': 'red', 'ray': 'blue', 'matthew': 'yellow'}
print(d)

# Counters with dictionaries:
# If the color is missing form the dict, return 0 and add 1.
colors = ['red', 'blue', 'white']
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print(d)  # d is now {‘blue': 1, 'white': 1, 'red': 1}

# Grouping with dictionaries):
names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']
d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
print(d)  # {5: ['roger', 'betty'], 6: ['rachel', 'judith'], 7: ['raymond', 'matthew', 'melissa', 'charlie']}

# Example 10 (pop item)
d = {'pito': 'rafael', 'sebee': 'sebastian', 'steph': 'stephanie'}
while d:
    key, value = d.popitem()
    print(key, '-->', value)


