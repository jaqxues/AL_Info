from C5_Fonctions.Ex5_2 import gcd
# Or: `from math import gcd`


def gcd3(a, b, c):
    return gcd(gcd(a, b), c)
