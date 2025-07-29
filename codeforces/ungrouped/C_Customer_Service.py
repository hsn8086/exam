# import sys

# sys.setrecursionlimit(114514)


# def search_mex(matrix, i, visited):
#     if i > len(matrix):
#         return i
#     rst = []
#     for j, a in enumerate(matrix):
#         if j in visited:
#             continue
#         if i in a:
#             vis = visited.copy()
#             vis.add(j)

#             rst.append(search_mex(matrix, i + 1, vis))
#     if rst:
#         return max(rst)
#     else:
#         return i


# def search_mex2(matrix, i, visited):
#     if i > len(matrix):
#         return i
#     rst = []
#     for j, a in enumerate(matrix):
#         if j in visited:
#             continue
#         if i == a[i]:
#             vis = visited
#             vis.add(j)
#             rst.append(search_mex(matrix, i + 1, vis))
#     if rst:
#         return max(rst)
#     else:
#         return i


# for _ in range(int(input())):
#     n = int(input())
#     suffix_sum = [[0] for _ in range(n)]
#     for i in range(n):
#         a = map(int, reversed(input().split()))
#         for an in a:
#             suffix_sum[i].append(suffix_sum[i][-1] + an)

#     print(search_mex(suffix_sum, 0, set()))
from bisect import bisect_left

for _ in range(int(input())):
    n = int(input())
    suffix = []
    for _ in range(n):
        a = map(int, reversed(input().split()))
        for i, v in enumerate(a):
            if v != 1:
                suffix.append(i)
                break
        else:
            suffix.append(n)
    suffix.sort()

    for i in range(n):
        idx = bisect_left(suffix, i)
        if idx >= n:
            print(i)
            break
        suffix[idx] = 0

    else:
        print(n)
