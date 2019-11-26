# n, m, l, h = tuple(map(int, input().split(" ")))
#
# k = int(input())
# values = []
# for _ in range(k):
#     values.append(tuple(map(int, input().split(" "))))
#
# assert 1 <= n <= 1e9 and 1 <= m <= 1e9
# assert 1 <= l <= min(10, n) and 1 <= h <= min(10, m)
# assert 0 <= k <= 100
# for (x, y, w) in values:
#     assert 1 <= x <= n and 1 <= y <= m
#     assert 0 <= w <= 1e9
#
# # for x1 in range(n - l + 1):
# #     for x2 in range(1, l):
# #         if x1 + x2 >= n:
# #             continue
# #         for x3 in range(0, l + 1):
# #             if x1 + x2 + x3 >= n:
# #                 continue
# #             print(x1, x1 + x2 + x3)
#
#
# # sum = 0
# # for (x, y, w) in values:
# #     if x <= n and y <= m and x < l and y < h:
# #        sum += w
# #
# # print(sum)
#
# # sums = []
# #
# #
# # def get_combinations(_list, l, rec_result=[]):
# #     if len(rec_result) == l:
# #         sums.append(sum(map(lambda x: x[2], rec_result)))
# #         return
# #     for x in range(len(_list)):
# #         if _list[x] in rec_result:
# #             continue
# #         _copy = rec_result[:]
# #         _copy.append(_list[x])
# #         get_combinations(_list, l, _copy)
# #
# #
# # print(get_combinations(values, l))
# # print(sums)
#
#
# # https://en.wikipedia.org/wiki/Maximum_subarray_problem

import os
import re
import fileinput
reg = re.compile("Ex\d*_\d*\.py")
test = True
for x in os.walk("/home/jaqxues/CodeProjects/PycharmProjects/AL_Info"):
    for y in x[2]:
        if reg.match(y):

            with fileinput.FileInput(x[0] + "/" + y, inplace=True) as file:
                for line in file:
                    print(line.replace('"', "'"), end='')

            print(x[0], y)
