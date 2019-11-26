n = int(input("Enter n: "))

iterations = 0

while n != 1:
    iterations += 1
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1

print("Number of iterations:", iterations)
