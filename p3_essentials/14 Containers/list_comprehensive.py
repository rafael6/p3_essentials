__author__ = 'rafael'

# Traditional
squares = []

for x in range(10):
    squares.append(x**2)
print(squares)

# list comprehensions
squares = [x**2 for x in range(10)]
print(squares)

# Traditional with condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even =[]
for x in numbers:
    if x % 2 == 0:
        even.append(x)
print(even)

# List comprehension with condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = [x for x in numbers if x % 2 == 0]
print(even)

# 2D list
board = [[0]*8 for _ in range(8)]
print(board)

# metrix example, grab first element

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

first = [x[0] for x in matrix]

print(first)


# Nested LC
matrix = [ range(0,5), range(5,10), range(10,15) ]


def eg1_for(matrix):
    flat = []
    for row in matrix:
        for x in row:
            flat.append(x)
    return flat


def eg1_lc(matrix):
    return [x for row in matrix for x in row ]


print(eg1_for(matrix))
print(eg1_lc(matrix))


print('NEXT')


# List comprehension with condition and function

def add_one(num):
    #print(num + 1)
    return num+1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = [add_one(x) for x in numbers if x % 2 == 0]

print(even)