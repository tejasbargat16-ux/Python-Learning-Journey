import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


shapes = [
    Rectangle(10, 5),
    Circle(7)
]

for shape in shapes:
    print("Area:", round(shape.area(), 2))
