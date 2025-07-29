import math
from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
a = map(int, input().split())
b = map(int, input().split())

b_mp = {v: i for i, v in enumerate(b)}

diffs = []

for i, v in enumerate(a):
    diff = abs(i - b_mp[v])
    diffs.append(diff)

ans_raw = math.gcd(*diffs)
ans = []
for i in range(1, ans_raw + 1):
    if ans_raw % i == 0:
        ans.append(i)
print(*ans, sep="\n")
