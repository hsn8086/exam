# import bisect
# def solve(kl: list[int]):
#     max_ = max(kl)
#     sum_list = []
#     current = 0
#     idx = 0
#     end = 3
#     while current != max_:
#         current += 1 if idx else 0
#         sum_list.append(current)

#         idx += 1
#         if idx == end:
#             idx = 0
#             end += 2

#     for k in kl:
#         yield bisect.bisect(sum_list,k)
# import math


# def solve(kl: list[int]):
#     for k in kl:
#         res = math.sqrt(k)
#         if res % 1 >= 0.5:
#             res = math.ceil(res)
#         else:
#             res = math.floor(res)
#         yield k + res
# def solve(kl: list[int]):
#     res_list = []
#     for k in kl:
#         n = 0
#         count = 0
#         while count != k:
#             n += 1
#             if n > len(res_list):
#                 res = 1
#                 for i in range(1, n + 1):
#                     if n % i == 0:
#                         res += 1
#                 res_list.append(res % 2)
#             count += res_list[n - 1]
#         yield n

import math
def isqrt_newton(n):
    x = 1
    decreased = False
    while True:
        nx = (x + n // x) // 2
        if x == nx or (nx > x and decreased):
            break
        decreased = nx < x
        x = nx
    return x


def solve(kl: list):
    for k in kl:
        yield k + math.ceil((isqrt_newton(1 + 4 * k) - 1) / 2)


num_of_tc = int(input())

kl = (int(input()) for _ in range(num_of_tc))
for i in solve(kl):
    print(i)

# kl=[i for i in range(100000)]
# for i,j in zip(solve(kl),solve2(kl)):
#     if i!=j:
#         print(i,j)
"""[0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]"""
