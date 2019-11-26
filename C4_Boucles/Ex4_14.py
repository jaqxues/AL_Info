n = int(input('Enter n: '))

# a)
for x in range(1, n + 1):
    print('*' * x)


print('=' * n * 2)

# b)
for x in range(1, n + 1):
    print(' ' * (n - x), end='')
    print('*' * x)


print('=' * n * 2)

# c)
for x in range(n):
    print(' ' * (n - x - 1), end='')
    print('*' * (1 + 2 * x))

print('=' * n * 2)

# d)
spaces = n // 2
for x in range(spaces + 1, 0, -1):
    print(' ' * x, end='')
    print('*' * (n - x * 2))
for x in range(0, spaces + 1):
    print(' ' * x, end='')
    print('*' * (n - x * 2))
