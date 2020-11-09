data = {}

with open('samples/notes.txt', 'r') as file:
    line = file.readline()
    while line != '':
        splitted = line.split(' ')
        if splitted[0] in data:
            data[splitted[0]] = (data[splitted[0]] + int(splitted[1])) / 2
        else:
            data[splitted[0]] = int(splitted[1])
        line = file.readline()

print('Number of student -- Average')
for key, value in sorted(data.items()):
    print(key, '\t\t\t', f'{value:.1f}')
