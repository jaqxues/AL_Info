from C6_Structures.Ex6_5 import get_polynomial

poly = get_polynomial()
a = int(input("Enter a (x - a): "))

previous = 0
new_values = []
for x in range(len(poly)):
    current = previous + poly[x]
    new_values.append(current)
    previous = current * a

print(new_values)
