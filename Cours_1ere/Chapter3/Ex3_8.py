from stack import Stack


def dec_2_bin_stack(n):
    if n == 0:
        return '0'
    s = Stack()
    tmp = n
    while tmp > 0:
        tmp, r = divmod(tmp, 2)
        s.push(r)
    res = ''
    while not s.is_empty():
        res += str(s.pop())
    return res


print(dec_2_bin_stack(100))
