from itertools import product
import sys
from collections import defaultdict

from random import randint

input = sys.stdin.readline

rnd = randint(57, 8086)
for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    cnt = defaultdict(int)

    for i, j in product(range(n), range(m)):
        now = matrix[i][j] + rnd
        cnt[now] = max(1, cnt[now])
        if i + 1 < n:
            if matrix[i + 1][j] + rnd == now:
                cnt[now] = 2
        if j + 1 < m:
            if matrix[i][j + 1] + rnd == now:
                cnt[now] = 2

    lst = sorted(cnt.values())
    lst.pop()
    if lst:
        print(sum(lst))
    else:
        print(0)
