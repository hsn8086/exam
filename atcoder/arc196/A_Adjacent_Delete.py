from random import choices
import sys
input=sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
i = 0
cnt = 0
while i < len(a) - 1:
    if i + 2 == len(a):
        cnt += abs(a.pop(i) - a.pop(i))
        i -= 3
    elif abs(a[i] - a[i + 1]) > abs(a[i + 1] - a[i + 2]):
        cnt += abs(a.pop(i) - a.pop(i))
        i -= 2
    if i < -1:
        i = -1

    i += 1
print(cnt)
