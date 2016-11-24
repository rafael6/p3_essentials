'''
Enumerate allows you to keep a count as you iterate through an object.
It does this by returning a tuple in the form (count,element)'''

lst = ['a', 'b', 'c']

for count, item in enumerate(lst):
    print(count, item)


print('Example 2, create a dictionary from a list containing the values ')
lst = ['a', 'b', 'c']


def d_list(l):
    return {key: value for value, key in enumerate(l)}

print(d_list(lst))

print('Example 3, crete returns a count if value of an item match its index.')
lst = [0, 2, 2, 1, 5, 5, 6, 10]

def count_match_index(l):
    return len([num for count, num in enumerate(l) if num == count])
print(count_match_index(lst))