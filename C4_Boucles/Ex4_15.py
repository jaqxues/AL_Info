n = int(input('Enter n: '))

# a)
for x in range(n):
    if n - 1 == 0 or x % (n - 1) == 0:
        print('*' * n)
        continue
    print('*' + ' ' * (n - 2) + '*')

print('=' * n * 2)

# b)
for x in range(n):
    if n - 1 == 0 or x % (n - 1) == 0:
        print('*' * n)
        continue
    print('*', end='')
    print(' ' * (x - 1), end='')
    print('*', end='')
    print(' ' * (n - 2 - x), end='')
    print('*')

print('=' * n * 2)

# c)
for x in range(n):
    if n - 1 == 0 or x % (n - 1) == 0:
        print('*' * n)
        continue
    print('*', end='')
    print(' ' * (n - 2 - x), end='')
    print('*', end='')
    print(' ' * (x - 1), end='')
    print('*')

print('=' * n * 2)

# d)
for x in range(n):
    string = 'X ' if x % 2 == 0 else ' X'
    print(string * (n // 2))
