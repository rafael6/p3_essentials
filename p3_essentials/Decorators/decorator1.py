class P:
    """Demonstrate how to do getters and setters with Python.

    To make sure we get an argument with the function call.
    Users have access to x, but internally is __x  """
    def __init__(self, x):
        # Below what triggers x.setter decorator.
        # The self.x below is NOT what the uses access when p1.x
        self.x = x

    # This what the users gets when p1.x
    # Returns the self.__x as p1.x (self.x) modified & provided by the setter function below.
    # self.__x is the only returned value in the class.
    @property  # It sets x as a class attribute (self.x)
    def x(self):  # The x here is what is referenced when p1.x below.
        return self.__x

    # The setter sets the value of self.__x
    # This is the setter for the property function.
    # This is called when a value is assigned to x
    # It can be use to normalize the bound input
    @x.setter
    def x(self, x): # It sets the value of __x from x which is used by the property
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

p1 = P(1002)
print(p1.x)
