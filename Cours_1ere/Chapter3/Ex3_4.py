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
        self.pa = Point('A', 0, 0) if pa is None else pa
        self.pb = Point('B', 3, 0) if pb is None else pb
        self.pc = Point('C', 0, 4) if pc is None else pc

    def __str__(self):
        return f'Triangle({",".join((self.pa, self.pb, self.pc))})'

    def set_random_data(self, min, max):
        self.pa, self.pb, self.pc = Point('random', min, max), Point('random', min, max), Point('random', min, max)

    def calculate_circumference(self):
        return self.pa.distance_to(self.pb) + self.pb.distance_to(self.pc) + self.pc.distance_to(self.pa)

    def show_type(self):
        distab, distbc, distca = self.pa.distance_to(self.pb), \
                                 self.pb.distance_to(self.pc), \
                                 self.pc.distance_to(self.pa)
