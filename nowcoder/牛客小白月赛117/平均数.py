from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())
a = Counter(map(int, input().split()))

if (a[-1] == 0 or a[1] == 0) and a[0] != n:
    print("NO")
else:
    print("YES")
