from math import sqrt
from collections import defaultdict
from random import shuffle

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(zip(map(int, input().split()), map(int, input().split())))
    shuffle(a)

    cnt = defaultdict(int)
    for x, r in a:
        for i in range(x - r, x + r + 1):
            cnt[i] = max(int(sqrt(r**2 - (x - i) ** 2)) * 2 + 1, cnt[i])

    print(sum(cnt.values()))
