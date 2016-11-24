'''
The methods in a class should represent things that are part of the class.
'''

class Duck: # Duck is the class
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck() # Donald is a Duck object therefore Donald is also self.
    donald.quack() # quack is an object attribute a method in this example.
    donald.walk() # The dot is used to reference and attribute of the object.

if __name__ == "__main__": main()
