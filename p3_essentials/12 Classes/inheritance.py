'''
In object-oriented programming, inheritance is when one class inherits the
properties of another class.

Inheritance -> Is A relationship
'''

class Animal:
    def talk(self):
        print('I talk')

    def walk(self):
        print('I walk')

    def clothes(self):
        print('I have clothes')


class Duck(Animal):  # Inherits all attributes from class Animal (Is a) relationship.
    def quack(self):
        print('Quaaack!')

    def walk(self):
        super().walk()  # To override the child walk() method with the parent walk() method
        print('Walks like a duck.')


class Dog(Animal):
    def clothes(self):
        print('I have dog clothes')

def main():
    print('\nDonald:')
    donald = Duck()
    donald.quack()
    donald.walk()  # The child walk() method overrides the parent walk() method, but super() method change this.
    donald.clothes()

    print('\nFido:')
    fido = Dog()
    fido.walk()
    fido.clothes()  # The child clothes() method overrides the parent clothes() method

if __name__ == "__main__": main()


print('\nExample 2:\n')
# Example 2
class Animal:
    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('Animal')

    def eat(self):
        print('Eating...')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def who_am_i(self): # Will override parent method
        print('Dog')

    def bark(self):
        print('Woof!')

Lala = Dog()
Lala
print()
Lala.who_am_i()  # Override parent method since child also has a who_am_i() method
Lala.eat()  # Use parent since child doesn't have the eat() method
Lala.bark()  # bark() method only in child class



