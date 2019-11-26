n = int(input("Enter n: "))
assert n >= 1

matrix = [[1 / (i + j + 1) for i in range(n)] for j in range(n)]

print(matrix)
