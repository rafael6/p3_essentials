# Evolution to Lambda expressions
# map return an iterator object, but we are casting to list to see it


def square(num):
    result = num**2
    return result

print(square(4))


def quare(num):
    return num**2

print(square(4))

def square(num): return num**2
print(square(4))

# Ex 1, one parameter
square = lambda num: num**3
print(square(4))

#Ex 2, two parameter
add_two = lambda num_1, num_2: num_1+num_2
print(add_two(2, 3))


# Ex 3, conditional expresion with function (print)
compare = lambda x: print('big') if x > 100 else print('small')
compare(25)
