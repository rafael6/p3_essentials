class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @width.deleter
    def width(self):
        del self._width

r = Rectangle(5, 6)
# automatically accesses getter, behind the scenes
print("Width: {:d}".format(r.width))

