a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
d = int(input('Enter d: '))

assert a <= b <= c

if d < a:
    a, b, c, d = d, a, b, c
elif d < b:
    b, c, d = d, b, c
elif d < c:
    c, d = d, c

print(f'{a} <= {b} <= {c} <= {d}')
