from random import randrange

n = int(input('Enter n: '))
values = [randrange(-10e20, 10e20) / 10e10 for _ in range(n)]
values.sort()

if len(values) % 2 != 0:
    median = values[len(values) // 2]
else:
    index = len(values) // 2
    median = (values[index - 1] + values[index]) / 2
print(values)
print('Median:', median)
