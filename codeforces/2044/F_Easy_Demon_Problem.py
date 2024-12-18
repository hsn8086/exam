import sys

input = sys.stdin.readline
n, m, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
qs_ = [int(input()) for _ in range(q)]
qs = dict((i, False) for i in qs_)
sum_a = sum(a)
sum_b = sum(b)
total = sum_a * sum_b

for i in range(n):
    for j in range(m):
        new_total = total - a[i] * sum_b - b[j] * sum_a + a[i] * b[j]
        if new_total in qs:
            qs[new_total] = True

for k in qs_:
    v = qs[k]
    if v:
        print("YES")
    else:
        print("NO")
