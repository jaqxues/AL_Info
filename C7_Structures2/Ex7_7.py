def f(_n):
    return _n // 2 if _n % 2 == 0 else 3 * _n + 1


def collatz(_n):
    assert _n > 0
    _values = []
    while _n != 1:
        _n = f(_n)
        _values.append(_n)
    _values.append(1)
    return _values


def max_collatz(_n):
    _values = [collatz(i) for i in range(1, _n + 1)]
    print(_values)
    return _values, len(max(_values, key=len)), max(max(_values, key=max))


print(collatz(14))
n = int(input('Enter n: '))
values, max_index, max_value = max_collatz(n)
print('Max length:', max_index)
print('Max Value:', max_value)
indices = list(map(len, values))
counts = []
for x in range(100):
    counts.append(indices.count(x))
print(counts)

SPACES = 4 + len(str(max(counts)))
for x in range(10):
    for y in range(1, 10 + 1):
        nb = x * 10 + y
        print(' ' * (SPACES - len(str(nb)) - len(str(counts[nb - 1]))), nb, '|', counts[nb - 1], end='')
    print()
