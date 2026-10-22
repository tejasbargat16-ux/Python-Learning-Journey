class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle1 = Rectangle(10, 5)

print("Length:", rectangle1.length)
print("Width:", rectangle1.width)
print("Area:", rectangle1.area())
