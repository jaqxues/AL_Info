from math import sqrt

n = int(input("Enter n: "))
assert 1 <= n <= 100

persons = {}
for x in range(n):
    persons[x + 1] = tuple(map(int, input().split(" ")))


def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def run_iteration(_persons):
    to_kill = []
    for (name1, person) in _persons.items():
        distances = {}
        for (name2, other) in _persons.items():
            if name1 is name2:
                continue
            distances[name2] = distance(*person, *other)

        targets = []
        current_lowest = float("inf")

        for name, d in distances.items():
            if d > current_lowest:
                continue
            elif d == current_lowest:
                targets.append(name)
            else:
                current_lowest = d
                targets = [name]

        if len(targets) == 1:
            to_kill.append(targets[0])

    return {name: person for (name, person) in _persons.items() if name not in to_kill}


counter = 0
old = persons
while True:
    new = run_iteration(old)
    if not new:
        print(counter + 1)
        print("+")
        break
    if len(new) == len(old):
        print(counter)
        print(" ".join(map(str, new.keys())))
        break
    old = new
    counter += 1
