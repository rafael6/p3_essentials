'''
data = input()

lc = [int(i) for i in data.split(',')]

print(lc)
'''

def add_one(num):
    #print(num + 1)
    return num+1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = [add_one(x) for x in numbers if x % 2 == 0]
print(even)
