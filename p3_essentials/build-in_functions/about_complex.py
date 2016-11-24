'''
complex() returns a complex number with the value real + imag*1j or converts a string or number to a complex number.

If the first parameter is a string, it will be interpreted as a complex number
and the function must be called without a second parameter. The second parameter
can never be a string. Each argument may be any numeric type (including complex).
If imag is omitted, it defaults to zero and the constructor serves as a numeric conversion
like int and float. If both arguments are omitted, returns 0j.
'''

# Example 1, two is the real part and three is the imaginary part
c = complex(2, 3)
print(c)

# OR

# Example 2, single string expression for the real and imaginary parts
c = complex('2+3j')
print(c)