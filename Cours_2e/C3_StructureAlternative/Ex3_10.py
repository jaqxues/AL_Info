n = int(input('Prime Number: '))

if (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0) and (n != 2 and n != 3 and n != 5 and n != 7) or (
        n == 0 or n == 1):
    print(n, 'is not a prime number')
else:
    print(n, 'is a prime number')
