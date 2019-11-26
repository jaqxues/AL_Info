a = int(input("Enter a: "))
b = int(input("Enter b: "))

while b != 0:
    a = a % b
    if b > a:
        a, b = b, a
print("GCD is", a)
