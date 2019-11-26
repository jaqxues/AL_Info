n = input("Enter n: ")

assert n.isdigit()

sum_digits = 0
for i in n:
    sum_digits += int(i)

print(f"Sum of the digits of {n}: {sum_digits}")

# print(sum(map(int, n)))
