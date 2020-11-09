e = 1e-10
h = e


def find_root(f):
    def f_prime(_x):
        return (f(_x + h) - f(_x - h)) / (2 * h)

    x = float(input('Enter x0: '))
    while abs(f(x)) > e:
        x = x - f(x) / f_prime(x)
    return x
