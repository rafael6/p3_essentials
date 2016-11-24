
# strings are immutable, so s and s1 are different objects
# format() returns a new string
# No need to know the type like %d since format uses repr() methos
s = 'This is {}, that is {}'
s1 = s.format(5, 10)
print(s is s1)

print('\n')

# You can specify positional arguments in the {}, but you don't have to
a, b = 5, 10
print('This is ten {1}, this is five {0}, and ten again {1}.'.format(5, 10))

print('\n')

# You can also use names
print('This is {beto}, this is {sebee}.'.format(beto=5, sebee=10))

print('\n')

# You can also use dictionary
d = dict(beto=5, sebee=10)
print('This is {beto}, this is {sebee}.'.format(**d))