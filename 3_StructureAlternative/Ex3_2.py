n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
n3 = int(input("Enter n3: "))

max_value = n1
if n2 > max_value:
    max_value = n2
elif n3 > max_value:
    max_value = n3

print("Maximal Value:", max_value)
