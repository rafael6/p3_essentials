class Duck:
    def __init__(self, value):
        self._v = value # This gets called when the instance is created. _v is a local variable

    def quack(self): # self is a reference to the object; donald in this example.
        print('Quaaack!', self._v)

    def walk(self):
        print('Walks like a duck.', self._v)

def main():
    donald = Duck(47) # The value is attached to the object not the class; this is encapsulation.
    donald.quack()
    donald.walk()
    frank = Duck(141)
    frank.quack()
    frank.walk()

if __name__ == "__main__": main()