from stack import Stack
from string import digits, ascii_uppercase

SYMBOLS = digits + ascii_uppercase


def dec2base_b_stack(n, b):
    if n == 0:
        return '0'
    s = Stack()
    tmp = n
    while tmp > 0:
        tmp, r = divmod(tmp, b)
        s.push(r)
    res = ''
    while not s.is_empty():
        res += SYMBOLS[s.pop()]
    return res


def base_b2dec_stack(n, b):
    tmp = 0
    idx = len(n)
    for c in n:
        tmp += SYMBOLS.index(c) * b ** (idx := idx - 1)
    return tmp


i = int(input("Enter a number in the base 10: "))
print(f'({i})_10 = ({dec2base_b_stack(i, 2)})_2')
b = int(input("Enter the base: "))
print(f'({i})_10 = ({dec2base_b_stack(i, b)})_{b}')
i = input(f"Enter a number in the base {b}: ")
print(f'({i})_{b} = ({base_b2dec_stack(i, b)})_10')
