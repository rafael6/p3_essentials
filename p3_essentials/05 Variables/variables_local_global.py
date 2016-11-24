# Global vs. local variables in functions

# This is a global variable
# You can consume it inside of a function such as print(f) or x = f + 1
# You cannot modified it unless you declare it global inside of a function.
f = 0
print(f)

def someFunction():
    global f  # To modify it; to reference is normal python scope
    f = "def"
    print(f)

someFunction()
print(f)

print()

# Perhaps a better way to change the value of global variable x
# Better than using global definition
x = 5
def example():
    y = x + 1
    return y

x = example()
print(x)