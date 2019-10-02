from math import sqrt

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

s = (a + b + c) / 2

print("Surface Area:", sqrt(s * (s - a) * (s - b) * (s - c)))
