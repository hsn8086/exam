# import math
# import bisect

# num_of_tc = int(input())
# for _ in range(num_of_tc):
#     n = int(input())
#     min_k = n / 2
#     a = map(int, input().split())
#     last = None
#     chance = 0 if n % 2 == 0 else 1
#     gap_list = []
#     for i, v in enumerate(a):
#         if i == 0:
#             last = v
#             continue
#         d = last - v
#         if d > min_k:
#             bisect.insort(d)
#         last = v
#     if gap_list:
#         if chance:
#             gap_list.pop(-1)


#     gap_sum = sum(gap_list)
#     add_k = (math.sqrt(min_k**2 + 4 * gap_sum) - min_k) / 2

#     print(math.ceil(min_k + add_k))
import math


num_of_tc = int(input())
for _ in range(num_of_tc):
    n = int(input())

    a = map(int, input().split())
    last = None
    chance = 0
    gap_list = []
    max_k = 0
    first_gap = 0
    for i, v in enumerate(a):
        if i == 0:
            last = v
            continue
        if i == 1:
            first_gap = v - last
        gap_list.append(v - last)
        max_k = max(v - last, max_k)
        if i == n - 1:
            if max_k == v - last:
                chance = 1
            if first_gap == max_k:
                chance = 1
        last = v

    gap_list.sort()
    if n % 2 == 1 and chance == 1 and gap_list:
        gap_list.pop(-1)

    if gap_list:
        print(gap_list[-1])
    else:
        print(1)
