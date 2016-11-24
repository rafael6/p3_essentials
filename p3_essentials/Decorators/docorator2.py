class Robot:
    """Demonstrate how to do getters and setters with Python
    with  a combination of public and private attributes"""

    def __init__(self, name, build_year, lk = 0.5, lp = 0.5 ):
        self.name = name # Public attribute
        self.build_year = build_year # Public attribute
        self.__potential_physical = lk # Private attribute
        self.__potential_psychic = lp # Private attribute

    @property  # It sets the function below as a class attribute
    def condition(self):  # condition is what is referenced when x.condition below is called.
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable!"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"

if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4 )
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)
    print(x.name)
    #print(x.lk) this will raise an Attribute error since lk is a private atribute.
