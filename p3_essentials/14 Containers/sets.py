# Sets are unordered collection of unique elements

# Add elements to a set
x = set()
x.add('a')
print(x)


# You can also cast a list
l = [1,1,1,2,2,2,3,3,3,4]
s = set(l)
print(s)

s = {'a', 'b', 'c'}
s.add('d')
print(s)
s.add('d')
print(s)