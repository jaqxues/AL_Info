n = int(input())

counter = 0
for x in range(-3, 4):
    if 0 <= n + 3 * x <= 9:
        counter += 1

print(counter)

