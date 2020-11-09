from time import perf_counter
from timeit import timeit
from profile import run


def _get_next_collatz(u):
    return u // 2 if u % 2 == 0 else 3 * u + 1


def collatz_it(u, n=100):
    for _ in range(n):
        u = _get_next_collatz(u)
    return u


def collatz_rec(u, n=100):
    if n <= 0:
        return u
    return collatz_rec(_get_next_collatz(u), n - 1)


def get_min_n_it(u):
    n = 0
    while u > 1:
        u = _get_next_collatz(u)
        n += 1
    return n


def get_min_n_rec(u, n=0):
    if u == 1:
        return n
    return get_min_n_rec(_get_next_collatz(u), n + 1)


if __name__ == '__main__':
    print("Testing Values for Iterative and recursive implementations")
    for x in range(1, 20):
        n = 100
        u = collatz_it(x, n)
        assert u == collatz_rec(x, n)
        print(f'u_0 = {x:2}\t\t\t-\tu_{n:<3} = {u:2}\t\t\t-\tu{get_min_n_rec(x):<3} = 1')

    '''
    Estimating the time necessary for a number is impossible given the unknown nature of high numbers.  This algorithm
    could be very performant for a number p = 2 ** n, but not for the number p + 1. The conditions (whether a number is
    even or odd) randomize the results too much to allow a reasonable time estimation, given that the conditions
    reappear in every single intermediate step. 
    '''

    print()
    u = 2 ** 10_000 + 7
    print("Measuring time taken to perform Collatz series (Iterative implementation) for u =", u)

    # Using time.perf_counter
    start = perf_counter()
    get_min_n_it(u)
    print("* Using time.perf_counter:", (perf_counter() - start))

    # Using timeit.timeit
    print("* Using timeit.timeit:", timeit(f'get_min_n_it({u})', 'from __main__ import get_min_n_it', number=10))

    # Using profile.run
    print("* Using profile.run")
    run(f'get_min_n_it({u})')
