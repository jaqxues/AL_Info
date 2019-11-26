filename = input("Enter filename: ")

values = []
with open(filename, "r") as file:
    line = file.readline()
    while line != "":
        for value in line.split(" "):
            values.append(int(value))
        line = file.readline()


counter = 0
values_len = len(values)
for i in range(values_len):
    if i + 1 < values_len and values[i] < values[i + 1]:
        counter += 1

print(counter)
