print('\nYou can iterate over a string')

s = 'hello'
for i in s:
    print(i, end='')

print('\nbut they are not iterators object, therefore no next()')
#print(next(s))# TypeError: 'str' object is not an iterator
print('You can use the next() method however.')

s_iter = iter(s)
print(next(s_iter), end='')
print(next(s_iter), end='')
print(next(s_iter), end='')
print(next(s_iter), end='')
print(next(s_iter), end='')