'''
When we define a function we can use **kwargs to indicate that all uncaptured
keyword arguments should be stored in a dictionary called kwargs.
'''

def main():
    testfunc(1, 2, 3, 11, 12, 13, one=21, two=22, four=23) # order of arguments must be: name, arbitrary tuple, key-word

def testfunc(this, that, other, *args, **kwargs):
    # **kwargs is actually a dict
    print(this, that, other, args, kwargs['one'], kwargs['two'], kwargs['four']) # 1 2 3 (11, 12, 13) 21 22 23

if __name__ == "__main__": main()
