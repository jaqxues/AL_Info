from string import ascii_uppercase
from random import choice, randint
from math import dist


class Point:
    def __init__(self, name, x, y):
        if name == "random":
            name = choice(ascii_uppercase)
            x, y = randint(x, y + 1), randint(x, y + 1)
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.name}({self.x}; {self.y})'

    def distance_to(self, other):
        return dist((self.x, self.y), (other.x, other.y))


class Triangle:
    def __init__(self, pa=None, pb=None, pc=None):
        """
        Not using Point('A', 0, 0) as a default parameters, since that would introduce mutable state into default
        parameters, which could lead to weird and hard to fix bugs. Consider this example:

        t = Triangle()
        print(t)
        t.pa.x = 10_000
        print(t)  # Expected Output
        print(Triangle())  # Unexpected. Any new triangle will use the point A at x=10_000
        """

        # Using a "normal" if else expression
        # self.pa = Point('A', 0, 0) if pa is None else pa
        # Using truthy and falsy values (pa evaluates as truthy (True) if it isn't None, [], '', {}, 0, or similar)
        # self.pa = pa if pa else Point('A', 0, 0)
        # Shorthand, using or as an expression (a or b evaluates to a if a else b)
        self.pa = pa or Point('A', 0, 0)
        self.pb = pb or Point('B', 3, 0)
        self.pc = pc or Point('C', 0, 4)

    def __str__(self):
        return f'Triangle({",".join(map(str, (self.pa, self.pb, self.pc)))})'

    def set_random_data(self, m_n, m_x):
        self.pa, self.pb, self.pc = Point('random', m_n, m_x), Point('random', m_n, m_x), Point('random', m_n, m_x)

    def calculate_circumference(self):
        return self.pa.distance_to(self.pb) + self.pb.distance_to(self.pc) + self.pc.distance_to(self.pa)

    def show_type(self):
        distab, distbc, distca = self.pa.distance_to(self.pb), \
                                 self.pb.distance_to(self.pc), \
                                 self.pc.distance_to(self.pa)
        if distab == distca == distbc:
            res = 'equilateral'
        elif distab == distca or distab == distbc or distca == distbc:
            res = 'isosceles'
        else:
            res = 'scalene'

        if distca ** 2 + distab ** 2 == distbc ** 2:
            res += f'and right-angled at vertex {self.pa}.'
        elif distab ** 2 + distbc ** 2 == distca ** 2:
            res += f'and right-angled at vertex {self.pb}.'
        elif distbc ** 2 + distca ** 2 == distab ** 2:
            res += f'and right-angled at vertex {self.pc}.'
        else:
            res += f'and not right-angled.'
        print("The", self, "is", res)
