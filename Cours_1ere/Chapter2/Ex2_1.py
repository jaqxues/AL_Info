from profile import run
from time import perf_counter
from timeit import timeit
from math import sqrt


def fib_it(n):
    """
    Time Complexity: range(n) -> O(n)
    """
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    return x


def fib_rec(n):
    """
    Time Complexity: O(2**n)
    """
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_dir(n):
    """
    Time Complexity: O(1)
    """
    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2  # - 1 / phi

    return round((1 / sqrt(5)) * (phi ** n - psi ** n))


if __name__ == '__main__':
    print("Testing Fibonacci Numbers")
    for i in range(20):
        f = fib_it(i)
        assert f == fib_rec(i) == fib_dir(i), "Values not matching"
        print(f'{i:5} - {f:5}')

    '''
    Mechanisms for measuring time accurately in Python:
    
    * Using the time Library (not recommended)
        * time.time: Unsuitable for accurate measuring (in given cases only precision of 1 second as stated in the docs)
        * time.perf_counter (time.process_time): Allows measuring Time deltas more accurately.
    * timeit.timeit: Executes a given statement n times and returns the average value of time per single execution.
    * profile.run: Profiles the method and shows a more in-depth analysis.
    
    It is generally not recommended to use time for measuring statements and functions in Python. Use timeit or profile.
    '''

    start = perf_counter()
    for _ in range(10):
        fib_rec(30)
    print('Measuring with time (recursive):', perf_counter() - start)

    print()
    print("Measuring with timeit")
    print("* Iterative:", timeit('fib_it(30)', 'from __main__ import fib_it', number=10))
    print("* Recursive:", timeit('fib_rec(30)', 'from __main__ import fib_rec', number=10))

    print()
    print("Measuring iterative and recursive implementations with profile.run")
    print("* Iterative")
    run('fib_it(30)')
    print("* Recursive")
    run('fib_rec(30)')
