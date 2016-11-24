'''
Decorators are special functions that return other functions and they are used
to modify the way that a function works.
'''


class Duck:

    def __init__(self, **kwargs):
        self.properties = kwargs # kwards is {"color": "blue"}

    '''
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key): # key is "color"
        return self.properties.get(key, None)# The value of "key" is blue; None is the default value

    '''
    #  this into an accessor for the variable called color
    @property
    def color(self):
        return self.properties.get('color', None)  # properties is {"color": "blue"}. Usage -> donald.color = 'blue'

    @color.setter
    def color(self, c):
        self.properties['color'] = c  # sets the value of key 'color' to c

    @color.deleter
    def color(self):
        del self.properties['color']  # deletes the value associated with key 'color'

def main():
    donald = Duck(color='green')
    print(donald.color)
    donald.color = 'blue'
    print(donald.color)

    del donald.color
    print(donald.color)

    donald.color = 'red'
    print(donald.color)


if __name__ == "__main__": main()
