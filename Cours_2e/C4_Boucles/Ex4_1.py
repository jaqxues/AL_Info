from math import sqrt

n = int(input('Enter n: '))
is_prime = True

if n <= 1:
    is_prime = False

for x in range(2, int(sqrt(n)) + 1):
    if n % x == 0:
        is_prime = False
        break

if is_prime:
    print(n, 'is a prime number')
else:
    print(n, 'is not a prime number')
