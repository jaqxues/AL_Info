current = 0

num_values = -1
sum_values = 0
while current >= 0:
    sum_values += current
    num_values += 1
    current = int(input(f'Enter number ({num_values}): '))

print('Sum:', sum_values, end='. ')
if num_values == 0:
    print('Average cannot be calculated')
else:
    print('Average:', sum_values / num_values)
