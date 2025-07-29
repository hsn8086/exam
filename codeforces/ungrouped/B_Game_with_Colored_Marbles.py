from random import shuffle
from math import ceil
from collections import Counter
import sys

inp = map(int, filter(bool, sys.stdin.read().split()))


for _ in range(next(inp)):
    n = next(inp)
    a = list(next(inp) for _ in range(n))
    shuffle(a)
    cnt = Counter(map(lambda x: x == 1, Counter(a).values()))
    print(ceil(cnt[True] / 2) * 2 + cnt[False])
