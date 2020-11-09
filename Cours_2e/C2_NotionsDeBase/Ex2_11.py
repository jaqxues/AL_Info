from math import sqrt

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

s = (a + b + c) / 2

print('Surface Area:', sqrt(s * (s - a) * (s - b) * (s - c)))
