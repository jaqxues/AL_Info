from Ex2_6 import get_random, selection_sort, quicksort
from timeit import timeit
from profile import run

if __name__ == '__main__':
    n = 10_000
    print(f'Measuring time for a list of {n} values')
    time = timeit(f'quicksort(get_random({n}, 0, 10 ** 4))', 'from __main__ import quicksort, get_random', number=100)
    print(f'* Using timeit:', time)
    print('* Using profile.run:')
    run(f'quicksort(get_random({n}, 0, 10 ** 4))')