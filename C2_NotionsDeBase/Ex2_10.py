r1 = int(input('Enter r1: '))
r2 = int(input('Enter r2: '))
r3 = int(input('Enter r3: '))
r4 = int(input('Enter r4: '))

print('Total Resistance of resistors in parallel:',
      1 / (1 / r1 + 1 / r2 + 1 / r3 + 1 / r4))

# New line to make it more readable
