n = int(input("Enter n: "))

MAX_LEN = len(str(n ** 2))
# str_format = "{:%dd}" % (MAX_LEN + 1)

for x in range(1, n + 1):
    for y in range(1, n + 1):
        # print(str_format.format(x * y), end="")
        print(" " * (MAX_LEN - len(str(x * y))), x * y, end="")
    print()


# With Headers:

# MAX_LEN_N = len(str(n))
# str_format_n = "{:%dd}" % MAX_LEN_N
#
# print(" " * (MAX_LEN_N - 1), "|", end="")
# for x in range(1, n + 1):
#     # print(str_format.format(x), end="")
#     print(" " * (MAX_LEN - len(str(x))), x, end="")
#
# print()
# print("-" * MAX_LEN_N + "|", end="")
# print("-" * (n * (MAX_LEN + 1)))
#
# for x in range(1, n + 1):
#     # print(str_format_n.format(x), end="")
#     print(" " * (MAX_LEN_N - len(str(x))), end="")
#     print(x, end="")
#
#     print("|", end="")
#
#     for y in range(1, n + 1):
#         # print(str_format.format(x * y), end="")
#         print(" " * (MAX_LEN - len(str(x * y))), x * y, end="")
#
#     print()
