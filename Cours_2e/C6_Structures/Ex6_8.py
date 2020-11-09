from math import sqrt

a = int(input('Enter a: '))
n = int(input('Enter n: '))

primes = []
current = a - 1

a = max(a, 2)
while True:
    current += 1
    for x in range(2, int(sqrt(current)) + 1):
        if current % x == 0:
            break
    else:
        primes.append(current)
        if len(primes) > n:
            break
        continue

print(primes)
