class Duck:
    def __init__(self, color='white'):
        self._color = color # _ local use only.

    def set_color(self, color):
        self._color = color

    def get_color(self):
        print(self._color)

def main():
    donald = Duck()
    donald.set_color('blue')
    donald.get_color()

if __name__ == "__main__": main()

###############################################################################
print('\nUsing a dictionary (kwargs)')

class Duck:
    def __init__(self, **kwargs):
        self.variables = kwargs # Assing dictionary to variables

    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)# None is the default value

def main():
    donald = Duck(feet=4) # Dictionary definition
    print(donald.get_variable('feet'))
    donald.set_variable('feet', 4) # Pass key and value as parameters
    print(donald.get_variable('feet'))
    donald.set_variable('color', 'red')
    print(donald.get_variable('color'))

if __name__ == "__main__": main()
