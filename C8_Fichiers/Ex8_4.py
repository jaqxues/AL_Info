with open('./samples/election.txt', 'r') as file:
    line = file.readline()
    lists = [0 for x in range(int(line))]

    line = file.readline()
    splitted = line.split(' ')
    candidates = []
    for list_of_candidate in splitted:
        candidates.append(int(list_of_candidate))

    line = file.readline()
    while line != '':
        for candidate in line.split(' '):
            lists[candidates[int(candidate) - 1] - 1] += 1
        line = file.readline()

print('Candidate - List')
for candidate in range(len(candidates)):
    print(candidate, candidates[candidate])
print('List: \t', '\t'.join(map(str, range(1, len(lists) + 1))))
print('Votes: \t', '\t'.join(map(str, lists)))

total_votes = sum(lists)
for _list in range(1, len(lists) + 1):
    print('List', _list, ':', f'{(lists[_list - 1] / total_votes * 100):.2f}%')
