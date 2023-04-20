class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length


a = Rectangle(5, 4)
print(a.area())