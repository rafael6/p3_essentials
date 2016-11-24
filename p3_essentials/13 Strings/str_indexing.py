# The first character is the 0 index
# Strings are immutable. Example s=[1] = 'a' is not allowable

s = 'Hello World'

# The entire string
print(s[:])

#From 6th character to end
print(s[6:])

# From character 1 thru 3
print(s[1:4])

# To print backwards
print(s[::-1])

# Steps; the third number is the step, default is step of 1
# print every other letter from the entire string
print(s[::2])

