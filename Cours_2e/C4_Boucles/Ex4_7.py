n = int(input('Enter n: '))

reverse = 0
tmp = n
while tmp > 0:
    digit = tmp % 10
    reverse = (reverse * 10) + digit
    tmp //= 10

if n == reverse:
    print(n, 'is a palindrome')
else:
    print(n, 'is not a palindrome')
