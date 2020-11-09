from math import gcd


class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.simplify()

    def __str__(self):
        return f'{self.n} / {self.d} ({self.n / self.d})'

    def set_d(self, d):
        self.d = d

    def simplify(self):
        val = gcd(self.n, self.d)
        if val != 1:
            self.n //= val
            self.d //= val

    def invert(self):
        self.n, self.d = self.d, self.n

    def add(self, other):
        self.n = self.n * other.d + other.n * self.d
        self.d *= other.d
        self.simplify()

    def subtract(self, other):
        self.add(Fraction(-other.n, other.d))

    def multiply(self, other):
        self.n *= other.n
        self.d *= other.d
        self.simplify()

    def divide(self, other):
        self.multiply(Fraction(other.d, other.n))
