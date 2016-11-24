# Use with any function that returns a boolean.
print('Example 1')
def even_check(num):
    if num % 2 == 0:
        return True
    else:
        return False

lst = range(10)

for i in filter(even_check, lst):
    print(i)

print('Example 2')
# Often used with lambda expressions
# Filter even numbers
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in filter(lambda num: num % 2 == 0, lst):
    print(i)

print('Example 3')
# Filter if number greater than 3
for i in filter(lambda num: num > 3, lst):
    print(i)


print('Example 4, create a list of words that start with the target letter.')

l = ['hello', 'there', 'how', 'are', 'you']


def filter_words(lst, letter):
    for i in filter(lambda word: word[0] == letter, lst):
        print(i)

filter_words(l, 'h')
