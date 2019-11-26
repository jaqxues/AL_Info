from math import gcd


def simplify(_f):
    div = gcd(*_f)
    if div == 1:
        return _f
    return _f[0] // div, _f[1] // div


def input_fraction(prefix=""):
    return int(input(prefix + "Numerator: ")), int(input(prefix + "Denominator: "))


if __name__ == '__main__':
    fraction = input_fraction()
    print(simplify(fraction))
