import sys
import random

input = sys.stdin.readline
n, m = map(int, input().split())
lst = []
for i in range(m):
    lst.append(tuple(map(int, input().split())))

lst.sort(key=lambda t: t[0] - t[1])
ans = 0
for a, b in lst:
    if n < a:
        continue
    cnt = (n - a) // (a - b)
    n = a + ((n - a) % (a - b))
    ans += cnt
    while n >= a:
        cnt, n = divmod(n, a)
        n += cnt * b
        ans += cnt



print(ans)
