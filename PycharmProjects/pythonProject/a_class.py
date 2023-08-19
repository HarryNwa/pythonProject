class Point:
    name = "Ken"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self):
        print("drawing...")
        return f"({self.a}, {self.b})"

    def __str__(self):
        return f"({self.a}, {self.b})"


Point.name = "joel"
p1 = Point(1, 2)
p2 = Point(5, 6)
print(p2.draw())
print(p1)
print(p2)
print(p2.name)





