def sum_of_integers(a, b):
    tmp = 0
    if a > b:
        a, b = b, a
    for x in range(int(a), int(b)):
        tmp += x
    print(tmp)
    return tmp
