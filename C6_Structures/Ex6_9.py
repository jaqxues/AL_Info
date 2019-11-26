from random import random

n = int(input("Enter n: "))
assert n >= 2

values = [random() * 100 for _ in range(n)]

product = 1
for value in values:
    product *= value

inverse_sum = 0
for value in values:
    inverse_sum += 1 / value

print("Arithmetic mean:", sum(values) / len(values))
print("Geometric mean:", product ** (1 / len(values)))
print("Harmonic mean:", len(values) / inverse_sum)
