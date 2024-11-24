# import bisect


# def solve(n, m, k, a: set, ops):
#     max_left_offset = 0
#     max_right_offset = 0
#     current = 0
#     a.sort()
#     for op in ops:
#         if op[0] == "1":
#             current += int(op[1])
#             max_right_offset = max(current, max_right_offset)
#         elif op[0] == "2":
#             current -= int(op[1])
#             max_left_offset = min(current, max_left_offset)
#         elif op[0] == "3":
#             left, right = (
#                 bisect.bisect_left(a, -max_left_offset - k),
#                 bisect.bisect_right(a, k - max_right_offset),
#             )

#             yield len(a[left:right])
# a = list(
#     filter(: set
#     )
# )
# yield len(a)
# rm_list = []

# for an in a:
#     if not (
#         -k <= an + max_left_offset <= k and -k <= an + max_right_offset <= k
#     ):
#         rm_list.append(an)
# for i in rm_list:
#     a.remove(i)
# yield len(a)
# count=0
# for i in a:
#     if -k <= i + max_left_offset <= k and -k <= i + max_right_offset <= k:
#         count+=1
# yield count
from collections import deque


def solve(n, m, k, a: deque, ops):
    max_left_offset = 0
    max_right_offset = 0
    current = 0
    for op in ops:
        if op[0] == "1":
            current += int(op[1])
            max_right_offset = max(current, max_right_offset)
        elif op[0] == "2":
            current -= int(op[1])
            max_left_offset = min(current, max_left_offset)
        elif op[0] == "3":
            while a and a[0] + max_left_offset < -k:
                a.popleft()
            while a and a[-1] + max_right_offset > k:
                a.pop()

            yield len(a)


n, m, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
d = deque(a)

ops = (input().split() for _ in range(m))
for i in solve(n, m, k, d, ops):
    print(i)
