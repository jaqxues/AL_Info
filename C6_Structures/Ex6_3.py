from random import randint

n = int(input('Enter n: '))
values = [randint(10, 25) for x in range(30)]

print('Occurrences:', values.count(n))

print(values[::-1])
