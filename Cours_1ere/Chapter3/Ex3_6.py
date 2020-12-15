from math import dist


class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def distance(self, p2):
        return dist((self.x, self.y), (p2.x, p2.y))

    def is_identical(self, p2):
        return self.x == p2.x and self.y == p2.y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Segment:
    def __init__(self, o=None, b=None):
        self.o = o or Point(0, 0)
        self.b = b or Point(1, 0)

    def get_boundary(self):
        return self.b

    def get_origin(self):
        return self.o

    def set_boundary(self, b):
        self.b = b

    def set_origin(self, o):
        self.o = o

    def get_length(self):
        return self.o.distance(self.b)

    def get_midpoint(self):
        o, b = self.o, self.b
        return Point((o.x + b.x) / 2, (o.y + b.y) / 2)

    def __str__(self):
        return f'segment [ {self.o}, {self.b} ]'


class Quadrilateral:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def get_diagonal1(self):
        return self.d1

    def get_diagonal2(self):
        return self.d2

    def set_diagonal1(self, d1):
        self.d1 = d1

    def set_diagonal2(self, d2):
        self.d2 = d2

    def is_parallelogram(self):
        return self.d1.get_midpoint().is_identical(self.d2.get_midpoint())

    def is_rectangle(self):
        return self.is_parallelogram() and self.d1.get_length() == self.d2.get_length()

    def __str__(self):
        d1, d2 = self.d1, self.d2
        return f'quad [ {d1.o}, {d2.o}, {d1.b}, {d2.b} ]'


p1 = Point(1, 9)
p2 = Point(2, 5)
print(p1)
print(p2)
print(Point())
p1.set_x(p2.get_y())
print(p1)
print(p1.distance(p2))
print(p2.is_identical(Point(2, 5)))
s1 = Segment(p1, p2)
print(s1.get_boundary())
print(s1)
s1.set_origin(Point(3, 7))
print(s1)
print(f'{s1.get_length():.3f}')
print(s1.get_midpoint())
print(Segment())
s2 = Segment(Point(7, 8), Point(5, 1))
q1 = Quadrilateral(s1, s2)
print(q1)
print(q1.is_parallelogram())
q1.set_diagonal1(Segment(Point(7, 1), Point(5, 8)))
print(q1)
print(q1.is_rectangle())
