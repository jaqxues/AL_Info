n = int(input("Enter n: "))

print(n, "=", end=" ")

# To avoid having "N = * x * ..."
needs_sign = False

while n != 1:
    for x in range(2, n + 1):
        if n % x == 0:
            if needs_sign:
                print(" * ", end="")
            print(x, end="")

            needs_sign = True

            n //= x
            break
