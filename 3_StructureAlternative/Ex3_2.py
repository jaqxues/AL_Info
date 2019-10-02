n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
n3 = int(input("Enter n3: "))

if (n1 >= n2 >= n3) or (n1 >= n3 >= n2):
    max_value = n1
elif n2 >= n3:
    max_value = n2
else:
    max_value = n3

print("Maximal Value:", max_value)
