from itertools import combinations

for _ in range(int(input())):
    k, a, b, c = map(int, input().split())
    lst = [a, b, c]
    max_ = 0
    for i in lst:
        if i <= k:
            max_ = max(max_, i)
    for i in combinations(lst, 2):
        if sum(i) <= k:
            max_ = max(max_, sum(i))
    if sum(lst) <= k:
        max_ = max(max_, sum(lst))
    print(k - max_)
