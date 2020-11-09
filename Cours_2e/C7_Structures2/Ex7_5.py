from math import gcd
from C7_Structures2.Ex7_4 import simplify, input_fraction

f1, f2 = (simplify(input_fraction(f'Fraction {i} - ')) for i in range(2))


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def amplify(_f, value):
    """
    :return: Fraction of form n / value
    """
    x = value // _f[1]
    return _f[0] * x, _f[1] * x


def sum_fractions(_f1, _f2):
    _lcm = lcm(_f1[1], _f2[1])

    _f1, _f2 = amplify(_f1, _lcm), amplify(_f2, _lcm)

    return simplify((_f1[0] + _f2[0], _lcm))


def dif_fractions(_f1, _f2):
    return sum_fractions(_f1, (-_f2[0], _f2[1]))


def multiply(_f1, _f2):
    return simplify((_f1[0] * _f2[0], _f1[1] * _f2[1]))


def divide(_f1, _f2):
    return multiply(_f1, _f2[::-1])


print(sum_fractions(f1, f2))
print(dif_fractions(f1, f2))
print(multiply(f1, f2))
print(divide(f1, f2))
