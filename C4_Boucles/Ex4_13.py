n = int(input("Enter n: "))

pi_4 = 1
current = 3
sign = -1
# Instead of using while loop and check the condition for each iteration, use a for loop with range --> better
# performance. But you need to know how far the for loop should go.

# Every term we add must be greater than precision / 4 (Since we multiply by 4 to get Pi). Let 1 / current be the
# smallest (last) term we need to add (or remove)
# Condition: 1 / current > precision / 4    | precision = 1 / 10 ** n
# <=> current < 4 / (1 / 10 ** n)
# <=> current < 4 * 10 ** n
# Since we add 2 every loop (iterations = current-1 / 2):
# We need 2 * 10 ** n iterations to get to a precision of n decimals
for _ in range(2 * 10 ** n + 1):
    pi_4 += sign / current
    current += 2
    sign *= -1

str_format = "{:.%df}" % n
print(pi_4 * 4)
print(str_format.format(pi_4 * 4))
