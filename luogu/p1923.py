import heapq
from typing import Iterable


def solve(n: int, k: int, an: Iterable):
    lst = [-10**9 for _ in range(k)]
    for a in an:
        heapq.heappushpop(lst, -a)
    return -lst[0]


n, k = map(int, input().split())
an = map(int, input().split())
print(solve(n, k, an))
"""
5 2
4 3 2 1 5

"""