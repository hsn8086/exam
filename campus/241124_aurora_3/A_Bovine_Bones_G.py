from itertools import count, product
from collections import Counter

s1, s2, s3 = map(int, input().split())

counter = Counter(
    a + b + c
    for a, b, c in product(range(1, s1 + 1), range(1, s2 + 1), range(1, s3 + 1))
)
min_ = float("+inf")
min_key = float("+inf")
first=-1
for m in counter.most_common():
    k, v = m
    if first == -1:
        first=v
    if v!=first:
        break
    if k < min_key:
        min_ = v
        min_key = k
print(min_key)
