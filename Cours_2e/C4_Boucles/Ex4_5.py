n = int(input('Enter n: '))
assert n >= 0

product = 1
for i in range(n, 1, -1):
    product *= i
print('Factorial of %d: %d' % (n, product))
