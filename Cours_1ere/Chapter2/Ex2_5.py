from functools import lru_cache
from math import factorial


def pascal_rec(n, k):
    assert 0 <= k <= n
    return 1 if k == 0 or k == n else pascal_rec(n - 1, k - 1) + pascal_rec(n - 1, k)


# Note that thanks to the behaviour of mutable default parameters, cache={} could be a default parameter. However,
# defining it outside the function makes the code more readable and clearer and is therefore preferred.
cache = {}


def pascal_rec_cached(n, k):
    # If already in cache, return from cache, else compute result, put into cache and return it
    if (n, k) in cache:
        return cache[n, k]
    result = 1 if k == 0 or k == n else pascal_rec_cached(n - 1, k - 1) + pascal_rec_cached(n - 1, k)
    cache[n, k] = result
    return result


# Using the existing functools.lru_cache decorator in Python
@lru_cache(maxsize=None)
def pascal_rec_lru_cache(n, k):
    assert 0 <= k <= n
    return 1 if k == 0 or k == n else pascal_rec_lru_cache(n - 1, k - 1) + pascal_rec_lru_cache(n - 1, k)


def pascal_it(n, k):
    assert 0 <= k <= n
    triangle = []
    for y in range(n + 1):
        row = []
        for x in range(y + 1):
            if x == 0 or x == y:
                row.append(1)
            else:
                row.append(triangle[y - 1][x - 1] + triangle[y - 1][x])
        triangle.append(tuple(row))
    return triangle[n][k]


def fact_it(n):
    x = 1
    for i in range(2, n + 1):
        x *= i
    return x


def fact_rec(n):
    # Without use - prefer Python's math.factorial function
    return 1 if n <= 1 else n * fact_rec(n - 1)


def pascal_dir(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


if __name__ == '__main__':
    n = int(input("Enter an integer N: "))
    for x in range(n):
        for y in range(x + 1):
            print(pascal_rec_cached(x, y), end=" ")
        print()
    for x in range(n, n + 10):
        print(sum((pascal_rec_cached(x, y) for y in range(x + 1))))

    print()
    a = int(input("Enter an integer a: "))
    m = int(input("Enter an integer M: "))
    for x in range(m):
        for y in range(x + 1):
            print(" " if pascal_rec_cached(x, y) % a == 0 else "*", end="")
        print()
