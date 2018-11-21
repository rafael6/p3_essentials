import sys

# Example 1:
# Run as: python3 sys_argv.py 10.1.1.1
print(sys.argv) # ['arguments.py', '10.1.1.1']


#Example 2:
# Run as: python3 sys_argv.py 10.1.1.1
if len(sys.argv) == 2:
     ip_addr = sys.argv.pop() # 10.1.1.1
     print("The IP address is {}".format(ip_addr))
else:
    print("error")


#Example 3:
# Run as: python3 sys_argv.py a b c
from sys import argv

script, first, second, third = argv

print("The scripts is called:", script)
print("Your first argument is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
