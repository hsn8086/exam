import bisect
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in map(int, input().split()):
    ans = bisect.bisect_left(a, i)
    if ans < n and a[ans] == i:
        print(ans + 1, end=" ")
    else:
        print(-1, end=" ")
