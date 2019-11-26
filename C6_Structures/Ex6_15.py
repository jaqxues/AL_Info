from C6_Structures.Ex6_5 import *

poly1 = get_polynomial()
poly2 = get_polynomial()


def sum_polynomial(_poly1, _poly2):
    _poly1, _poly2 = _poly1[::-1], _poly2[::-1]

    if len(_poly2) > len(_poly1):
        _poly1, _poly2 = _poly2, _poly1
    new_poly = _poly1[:]
    for d in range(len(_poly2)):
        new_poly[d] = _poly1[d] + _poly2[d]
    return new_poly[::-1]


def multiply_polynomial(_poly1, _poly2):
    _poly1, _poly2 = _poly1[::-1], _poly2[::-1]

    if len(_poly2) > len(_poly1):
        _poly1, _poly2 = _poly2, _poly1

    new_poly = [None for _ in range(len(_poly1) + len(_poly2) - 1)]

    for term1 in range(len(_poly1)):
        for term2 in range(len(_poly2)):
            degree = term1 + term2
            value = _poly1[term1] * _poly2[term2]
            if new_poly[degree] is None:
                new_poly[degree] = value
            else:
                new_poly[degree] += value

    return new_poly[::-1]


def dif_polynomial(_poly1, _poly2):
    return sum_polynomial(_poly1, list(map(lambda x: -x, _poly2)))


print(format_polynomial(sum_polynomial(poly1, poly2)))
print(format_polynomial(dif_polynomial(poly1, poly2)))
print(format_polynomial(multiply_polynomial(poly1, poly2)))
