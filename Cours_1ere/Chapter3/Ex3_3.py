from math import factorial, sqrt

class Number:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f'Value is {self.val}'

    def set_value(self, val):
        self.val = val

    def factorial(self):
        return factorial(self.val)

    def sum_of_divisors(self):
        if self.val == 1:
            return 1
        return sum(x + self.val // x for x in range(1, int(sqrt(self.val)) + 1) if self.val % x == 0)

    def reverse(self):
        return Number(int(str(self.val)[::-1]))
        # tmp = self.val
        # r = 0
        # while tmp > 0:
        #     tmp, rem = divmod(tmp, 10)
        #     r = 10 * r + rem
        # return Number(r)

    def is_square(self):
        return sqrt(self.val).is_integer()

    def is_prime(self):
        return self.sum_of_divisors() == self.val + 1

    def is_perfect(self):
        return self.sum_of_divisors() == 2 * self.val

    def is_palindrome(self):
        return self.reverse().val == self.val

    def is_amicable_to(self, other):
        return self.sum_of_divisors() == other.sum_of_divisors() == (self.val + other.val)


for x in range(10):
    for y in range(10):
        print(x, y, Number(x).is_amicable_to(Number(y)))
