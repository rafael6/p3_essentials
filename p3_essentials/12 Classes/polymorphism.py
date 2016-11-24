'''
Polymorphism is the practice of using one object of one particular class as if
it were another object of another class.
'''

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):  # must have a common interface
        print('The duck cannot bark')

    def fur(self):  # must have common interface
        print('The duck has feathers')


class Dog:
    def bark(self):
        print('woof!')

    def fur(self):
        print('The dog has fur')

    def quack(self):
        print('The dog cannot quack.')

    def walk(self):
        print('Walks like a dog')

def main():
    donald = Duck()
    fido = Dog()
    # as long as donald implements the interface that is being used in this function, it will still work

    # the objects in Python don't actually care what the name of the class is. When you use an object,
    # duck typing, because the types in Python, cat in this example just a reference everything is an object.

    # Any object of any class that implements the interface that's expected by any function can be used by
    #  that function.

    # any object that implements those methods will work in that function regardless of what its type is
    in_the_forest(donald)
    in_the_pond(fido)

# Expect an object that have a bark and fur interfaces.
def in_the_forest(cat):
    cat.bark()
    cat.fur()

# Expect an object that have a quack and walk interfaces.
def in_the_pond(cat):
    cat.quack()
    cat.walk()



if __name__ == "__main__": main()

