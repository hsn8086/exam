from math import ceil, floor
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    ct = Counter(input())
    print(ceil(ct["-"] / 2) * floor(ct["-"] / 2) * ct["_"])
