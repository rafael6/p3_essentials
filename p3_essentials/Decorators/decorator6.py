'''
Decorators are special functions that return other functions and they are used
to modify the way that a function works.
'''

properties = {}

def get():
    return properties

#  Accessor for class variable named color
@property
def color():
    return get()  # properties is {"color": "blue"}. Usage -> donald.color = 'blue'

@color.setter
def color(c):
    properties['color'] = c  # sets the value of key 'color' to c

@color.deleter
def color():
    del properties['color']  # deletes the value associated with key 'color'


print(color)

'''
donald = Duck(color='green')  # Triggers the @color.setter
print(donald.color)  # Triggers  @property
donald.color = 'blue'  # Triggers the @color.setter
print(donald.color)  # Triggers  @property
del donald.color   # Triggers  @color.deleter
print(donald.color)  # Triggers  @property
donald.color = 'red'  # Triggers the @color.setter
print(donald.color)  # Triggers  @property
'''