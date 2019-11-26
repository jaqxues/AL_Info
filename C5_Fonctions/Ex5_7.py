e = 1e-10
h = e


def find_root(f):
    def f_prime(x):
        return (f(x + h) - f(x - h)) / (2 * h)

    x = float(input("Enter x0: "))
    while abs(f(x)) > e:
        x = x - f(x) / f_prime(x)
    return x
