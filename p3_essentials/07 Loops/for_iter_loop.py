counter = 0

def test():
    global counter
    counter += 1
    return counter

for i in iter(test, 5):
    print(i)
