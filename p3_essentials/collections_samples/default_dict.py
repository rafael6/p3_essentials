from collections import defaultdict
'''
default dict doesn't thrown an error if you query a particular key for its value, instead
creates the key in the dictionary with whatever default value you assign.
'''

d = {'k1': 1}
# print(d['k2'])  # KeyError: 'one'

# default value object example. creates key 'one' which returns itself
dd = defaultdict(object)
print(dd['one']) #  <object object at 0x7f3b0bfa0080>
for i in dd:
    print(i) #  one

# The key is 'open', the value is whatever the function is returning
dd = defaultdict(lambda: 0)  # this lambda function just returns a 0
print(dd['one'])  # 0


print(dd)  # defaultdict(<function <lambda> at 0x7f4314a5fbf8>, {'one': 0})