x = float(input('Enter x: '))
n = int(input('Enter n: '))


if n <= 0:
    if x == 0:
        print('Negative power of 0 not possible')
    else:
        result = 1
        for i in range(-n):
            result /= x
        print(result)
else:
    result = 1
    for i in range(n):
        result *= x
    print(result)

# Or:
# result = 1
# if n == 0:
#     print('Negative power of 0 not possible')
# else:
#     for _ in range(abs(n)):
#         result *= x
#
# if n < 0:
#     result = 1 / result
# print('Result:', result)
