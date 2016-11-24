from functools import reduce

print('Example 1, add elements in a list.')
'''
This is what the reduce function below is doing
lst = [47, 11, 42, 13]

      47 + 11 = 58
                58 + 42 = 100
                          100 + 13 = 113
'''

lst = [47, 11, 42, 13]
print(reduce(lambda x,y: x+y, lst))


print('Example 2, find the max value in a list of numbers.')
lst = [1, 2, 30, 40, 50]
print(reduce(lambda a,b: a if (a > b) else b, lst))


print('Example 3, Take a list of number a return the number that they correspond to')

def digits_to_num(digits):
    return reduce(lambda x,y: x*10 + y, digits)

print(digits_to_num([1,2,3,4,5]))