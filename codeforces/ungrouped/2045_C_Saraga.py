# import sys

# a = sys.stdin.readline().strip()
# b = sys.stdin.readline().strip()

# max_ri = 0
# min_li = len(a)
# for i, v in enumerate("." + a[1:]):
#     if max_ri - min_li + i > len(b):
#         break
#     r_idx = b[:-1].rfind(v, max(max_ri - min_li + i, 0))
#     if r_idx != -1:
#         max_ri = r_idx
#         min_li = i
# if max_ri == 0 and min_li == len(a):
#     print(-1)
# else:
#     print(a[:min_li] + b[max_ri:])
import sys
from collections import defaultdict

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

a_opi = defaultdict(lambda: len(a))
b_opi = defaultdict(lambda: 0)

for i, v in enumerate("." + a[1:]):
    a_opi[v] = min(i, a_opi[v])
for i, v in enumerate(b[:-1]):
    b_opi[v] = max(i, b_opi[v])

left = len(a)
right = 0

for v, i in a_opi.items():
    if v not in b_opi:
        continue
    l_ = i
    r_ = b_opi[v]

    if l_ - r_ < left - right:
        left = l_
        right = r_
if left == len(a) and right == 0:
    print(-1)
else:
    print(a[:left] + b[right:])
