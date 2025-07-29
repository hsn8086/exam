from collections import Counter
from itertools import product
import sys

input = sys.stdin.readline
n = int(input())
a_cnt = Counter(map(int, input().split()))
max_cnt = 0
for u, v in product(a_cnt, repeat=2):
    if u == v and a_cnt[u] < 2:
        continue
    cnt = 0
    a_cnt_cpy = a_cnt.copy()
    a_cnt_cpy[u] -= 1
    a_cnt_cpy[v] -= 1
    while a_cnt_cpy[u + v]:
        a_cnt_cpy[u + v] -= 1
        u, v = v, u + v
        cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt + 2)
