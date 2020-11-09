def ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))


def ackermann_optimized(m, n):
    """
    Optimizing Ackermann by "Direct Computation"
    Calculating Ackermann more efficiently by replacing frequently calculated recursive steps with a simple formula.

    Examples for (1, m), (2, m) and (3, m):

    A(0, n) = n + 1

    A(1, n)
    = A(0, A(1, n - 1))
    = 1 + A(1, n - 1)
    = 1 + A(0, A(1, n - 2))
    = 1 + 1 + A(1, n - 2)
    ...
    = n + A(1, 0)
    = n + A(0, 1)
    = n + 1 + 1
    = n + 2

    A(2, n)
    = A(1, A(2, n - 1))
    = 2 + A(2, n - 1)
    = 2 + A(1, A(2, n - 2))
    = 2 + 2 + A(2, n - 2)
    ...
    = 2 * n + A(2, 0)
    = 2 * n + A(1, 1)
    = 2 * n + 3

    A(3, n)
    = A(2, A(3, n - 1))
    = ...
    = 8 * (2 ** n) - 3
    """
    if m == 0:
        return n + 1
    if m == 1:
        return n + 2
    if m == 2:
        return 2 * n + 3
    if m == 3:
        return 8 * 2 ** n - 3
    if n == 0:
        return ackermann_optimized(m - 1, 1)
    return ackermann_optimized(m - 1, ackermann_optimized(m, n - 1))


if __name__ == '__main__':
    for m in range(4):
        for n in range(6):
            a = ackermann(m, n)
            assert a == ackermann_optimized(m, n), "Calculated values not matching"
            print(f"A( m = {m:2}  ; n = {n:2} )\t= {a:6}")
