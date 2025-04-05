from itertools import chain
# from bisect import bisect
# from random import randint


# def check(a, x):
#     rst = bisect(a, x)
#     if a[rst - 1] == x:
#         return True
#     return False


# def abp(c, d, x):
#     for i, v in enumerate(c):
#         idx = bisect(d, v - x)
#         if d[idx - 1] == v - x:
#             return i, idx - 1
#     return None


# for _ in range(int(input())):
#     n = int(input())
#     b = sorted(map(int, input().split()))
#     c = b[n:]
#     d = b[:n]
#     rst = sum(i - j for i, j in zip(c, d))
#     idx = bisect(b, rst)
#     if b[idx - 1] == rst:
#         # while True:
#         #     rep_c_i = randint(0, n - 1)
#         #     rep_d_i = randint(0, n - 1)
#         #     rep_c = c[rep_c_i]
#         #     rep_d = d[rep_d_i]
#         #     if rst - 2 * (rep_c - rep_d) > 0 and not check(
#         #         b, rst - 2 * (rep_c - rep_d)
#         #     ):
#         #         c[rep_c_i], d[rep_d_i] = d[rep_d_i], c[rep_c_i]
#         #         print(
#         #             rst - 2 * (rep_c - rep_d),
#         #             *chain.from_iterable((i, j) for i, j in zip(c, d)),
#         #         )
#         #         break
#         ptr = idx - 1
#         ty = b[ptr]
#         while True:
#             while ty == b[ptr]:
#                 ty -= 2
#                 while ptr>0 and ty < b[ptr]:
#                     ptr -= 1
#             abd_rst = abp(c, d, (rst - ty) // 2)
#             if abd_rst:
#                 i, j = abd_rst

#                 c[i], d[j] = d[j], c[i]

#                 print(ty, *chain.from_iterable((i, j) for i, j in zip(c, d)))
#                 break
#             ty -= 1
#     else:
#         print(rst, *chain.from_iterable((i, j) for i, j in zip(c, d)))
import sys


for _ in range(int(input())):
    n = int(input())
    b = sorted(map(int, input().split()))
    d = b[::2]
    c = b[1::2]
    bset = set(b)
    s = sum(c) - sum(d)
    if s in bset:
        for i in range(n - 1):
            sel_c, sel_d = c[i], d[i + 1]
            c = s - 2 * (sel_d - sel_c)

            if c > 0 and c not in bset:
                c[i], d[i + 1] = d[i + 1], c[i]
                s = c
                break
    # bset = set(b)
    # if s in bset:
    #     found = False
    #     if not found:
    #         for i in range(min(n, 200)):
    #             if found:
    #                 break
    #             for j in range(min(n, 200)):
    #                 candidate = s - 2 * (c[i] - d[j])
    #                 if candidate > 0 and candidate not in bset:
    #                     s = candidate
    #                     c[i], d[j] = d[j], c[i]
    #                     found = True
    #                     break

    print(s, *chain.from_iterable((i, j) for i, j in zip(c, d)))
