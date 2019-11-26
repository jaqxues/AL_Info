a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
# Suppose c > a and c > b
if c ** 2 == a ** 2 + b ** 2:
    print("Right Triangle")
else:
    print("Not a right triangle")
