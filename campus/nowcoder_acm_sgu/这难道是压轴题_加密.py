from collections import Counter

n = int(input())
a = list(input().split())
mid = Counter(i[1:-1] for i in a)
fe = Counter(i[0] + i[-1] for i in a)
rst = n * (n - 1)

for i in a:
    m = i[1:-1]
    f = i[0] + i[-1]

    if mid[m] > 1:
        rst -= mid[m] - 1
    if fe[f] > 1:
        rst -= fe[f] - 1
    if mid[m] > 1 and fe[f] > 1:
        rst -= 2 * (fe[f] - 1) * (mid[m] - 1)
print(rst)
