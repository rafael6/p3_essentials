class Circle():
    pi = 3.14  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Object attribute alternative to radius
        self.perimeter = 2 * Circle.pi * self.radius  # Object attribute alternative to perimeter

    def area(self):
        return (self.radius**2) * Circle.pi

    def get_perimeter(self):  # get method alternative to perimeter
        return 2 * Circle.pi * self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_radius(self): # get method alternative to radius
        return self.radius


small_circle = Circle(10)
print(small_circle.radius)
print(small_circle.area())

small_circle.set_radius(15)
print(small_circle.area())
print(small_circle.radius)  # object attribute alternative to radius
print(small_circle.get_radius())  # get method alternative to radius

large_circle = Circle(100)
print(large_circle.get_perimeter())
print(large_circle.perimeter)