n1 = int(input('Enter n1: '))
n2 = int(input('Enter n2: '))

if (n1 > 0 and n2 < 0) or (n1 < 0 and n2 > 0):
    # only one number is negative and other number is not null
    print('Negative Product')
else:
    # either none of the numbers are positive or both of them are
    print('Positive Product')

print(n1 < 0, n2 < 0)

if (n1 < 0 and n2 < 0) or (n1 < 0 and 0 < n2 < -n1) or (n2 < 0 and 0 < n1 < -n2):
    # if both numbers are negative or the number with greatest absolute value is negative
    print('Negative Sum')
else:
    print('Positive Sum')
