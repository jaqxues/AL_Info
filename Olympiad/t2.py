a = int(input("Enter a: "))
b = int(input("Enter b: "))

assert a <= b
assert 1 <= a <= 10_000_000
assert 1 <= b <= 10_000_000

has_found = False

for x in range(a, b + 1):
    str_num = str(x)
    n = len(str_num)
    total = 0
    for num in str_num:
        total += int(num) ** n
    if x == total:
        has_found = True
        print(x)

if not has_found:
    print("Rien")

