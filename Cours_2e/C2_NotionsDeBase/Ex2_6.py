n1 = int(input('Enter n1: '))
n2 = int(input('Enter n2: '))

# Version 1
tmp = n1  # temporary value
n1 = n2
n2 = tmp

# Version 2
n1, n2 = n2, n1

# Additional Version 3 (swap without additional variable or parallel assignment)
n1 += n2
n2 = n1 - n2
n1 -= n2

print(f'Swapped... New Values: n1: {n1}, n2: {n2}')
