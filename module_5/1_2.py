class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def len(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f'{self.x},{self.y}'


p1 = Point(4, 2)
p2 = Point(1, 1)

print(p1 + p2)
print(p1 - p2)
print(p1 * p2)
print(p1.len(), p2.len())

