from itertools import permutations
from math import log


def check(a, b, n, m):
    cnt = 0
    for i, v in enumerate(reversed(a), 0):
        cnt += v * 7**i
    if cnt >= n:
        return False
    cnt = 0
    for i, v in enumerate(reversed(b), 0):
        cnt += v * 7**i
    if cnt >= m:
        return False
    return True


n, m = map(int, input().split())
ln = int(log(max(n - 1, 1), 7)) + 1
lm = int(log(max(m - 1, 1), 7)) + 1
# if ln + lm > 8:
#     print(0)
#     exit(0)

cnt = 0
for d in permutations([0, 1, 2, 3, 4, 5, 6], ln + lm):
    if check(d[:ln], d[ln:], n, m):
        cnt += 1
print(cnt)
