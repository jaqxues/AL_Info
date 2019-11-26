def f(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


def collatz(n):
    assert n > 0
    values = []
    while n != 1:
        n = f(n)
        values.append(n)
    values.append(1)
    return values


def max_collatz(n):
    values = [collatz(x) for x in range(1, n + 1)]
    print(values)
    return values, len(max(values, key=len)), max(max(values, key=max))


print(collatz(14))
n = int(input("Enter n: "))
values, max_index, max_value = max_collatz(n)
print("Max length:", max_index)
print("Max Value:", max_value)
indices = list(map(len, values))
counts = []
for x in range(100):
    counts.append(indices.count(x))
print(counts)

SPACES = 4 + len(str(max(counts)))
for x in range(10):
    for y in range(1, 10 + 1):
        nb = x * 10 + y
        print(' ' * (SPACES - len(str(nb)) - len(str(counts[nb - 1]))), nb, "|", counts[nb - 1], end="")
    print()
