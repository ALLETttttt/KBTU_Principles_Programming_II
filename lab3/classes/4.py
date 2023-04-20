class Point:
    def __init__(self, x, y):
        self.x1 = x
        self.y1 = y

    def show(self):
        print(self.x1, self.y1)

    def move(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    def dist(self):
        return ((self.x2-self.x1)**2 + (self.y2-self.y1)**2)**0.5


a = Point(5, 7)
a.move(2, 8)
print(a.dist())




