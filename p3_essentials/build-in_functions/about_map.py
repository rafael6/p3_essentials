# Map a function to an iterable object; run the function for each item in the iterator object

print('Example 1')
def fahrenheit(c):
    return (9.0/5)*c + 32

temps = [0, 64, 80, 93]

print(list(map(fahrenheit, temps)))  # With Python 3 must cast map to a list

print('Same as above but using lambda expression which is more common with map.')
print(list(map(lambda c: (9.0/5)*c + 32, temps)))


print('Example 2, adding the elements from each list')
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

m = map(lambda i,j: i+j, list_1, list_2)

for i in m:
    print(i)


print('Example 3, create a function which finds the lenght of each world in the phrase.')
def word_lenght(p):
    return list(map(len, p.split()))

print(word_lenght('How long are the words in this phrase'))