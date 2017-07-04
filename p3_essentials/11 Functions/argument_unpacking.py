# Argument unpacking
d = {'y': 3, 'x': 2}
l = [5, 7]


def testing(x, y):
    print(x, y)

testing(**d)
testing(*l)
