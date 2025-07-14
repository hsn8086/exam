from collections import Counter

n, m, k, l, d = map(int, input().split())
ct_x = Counter()
ct_y = Counter()

for _ in range(d):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2:
        ct_y[min(y1, y2)] += 1
    else:
        ct_x[min(x1, x2)] += 1

print(*sorted(i for i, _ in ct_x.most_common(k)))
print(*sorted(i for i, _ in ct_y.most_common(l)))
