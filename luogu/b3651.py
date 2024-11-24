n, k = map(int, input().split())
_sum = 0
a = map(int, input().split())
for i, v in enumerate(a):
    if i + 1 == k:
        v = -v
    _sum += v

print(_sum)
