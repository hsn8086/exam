n, k = map(int, input().split())
a = map(int, input().split())
b = map(int, input().split())
lst = [ai // bi for ai, bi in zip(a, b)]
if sum(lst) < k:
    print(*[0 for _ in range(n)])
    import sys

    sys.exit(0)
rst = []
for e in lst[::-1]:
    if e < k:
        rst.append(e)
        k -= e
    else:
        rst.append(k)
        k = 0
print(*rst[::-1])
