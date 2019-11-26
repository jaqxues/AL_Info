from random import randint

values = []

for x in range(6):
    value = int(input(f"Enter a number ({x})"))
    assert 1 <= value <= 49
    assert value not in values
    values.append(value)

new_values = []
while True:
    if len(new_values) == 6:
        break
    new_value = randint(1, 49)
    if new_value not in new_values:
        new_values.append(new_value)

counter = 0
for x in range(6):
    if values[x] == new_values[x]:
        counter += 1
print("Correct Numbers:", counter)
