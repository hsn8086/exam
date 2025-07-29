# import heapq

# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = sorted(enumerate(a), key=lambda t: t[1])
#     hq = []
#     vis = set()
#     while b:
#         i, v = b.pop()
#         i_ = i
#         min_ = float("+inf")
#         while 0 <= i_ < len(a) and a[i_] < v:
#             i_ -= 1
#             min_ = min(min_, a[i])

#             if (min_ + v) in vis:
#                 continue
#             vis.add(min_ + v)
#             heapq.heappush(hq, (min_ + v))

#         i_ = i - 1
#         min_ = float("+inf")
#         while 0 <= i_ < len(a) and a[i_] <= v:

#             i_ += 1
#             min_ = min(min_, a[i])
#             if (min_ + v) in vis:
#                 continue
#             vis.add(min_ + v)
#             heapq.heappush(hq, min_ + v)


#     # print(hq)

#     print(heapq.nlargest(k, hq))
import heapq
from itertools import chain


def pros(a: list):
    for i, v in enumerate(a):
        while True:
            i -= 1
            if i < 0 or v > a[i]:
                break
            elif v <= a[i]:
                yield v + a[i]


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    q = [0] * k
    for i in map(lambda x: 2 * x, a):
        heapq.heappushpop(q, i)
    for i, v in enumerate(a):
        while True:
            i -= 1
            if i < 0 or v > a[i]:
                break
            elif v <= a[i]:
                heapq.heappushpop(q, v + a[i])
    for i, v in enumerate(a[::-1]):
        while True:
            i -= 1
            if i < 0 or v > a[::-1][i]:
                break
            elif v <= a[::-1][i]:
                heapq.heappushpop(q, v + a[::-1][i])

    print(q[0])
