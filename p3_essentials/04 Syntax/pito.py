#!/usr/bin/env python3


class Car():
    """This is a basic class construct.
    """
    def __init__(self, brand, doors, model='320'):
        self.brand = brand
        self.doors = doors
        self.model = model

    def description(self):
        """This methods returns a dictionary.
        """
        return {'Brand': self.brand, 'Doors': self.doors, 'Model': self.model}


def main():
    """This is the main function.
    """
    my_car = Car('BMW', '4')
    for k, v in sorted(my_car.description().items()):
        print(k + ':', v)

if __name__ == "__main__":
    main()