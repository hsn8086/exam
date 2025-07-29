from collections import Counter

a = list(map(lambda s: int(s) % 3, input()))
cnt = Counter(a)

nd = sum(a) % 3
# print(nd,a)
if nd == 2 and cnt[2] >= 1 and len(a) > 1:
    print(1)
elif nd == 2 and cnt[1] >= 2 and len(a) > 2:
    print(2)
elif nd == 1 and cnt[1] >= 1 and len(a) > 1:
    print(1)
elif nd == 1 and cnt[2] >= 2 and len(a) > 2:
    print(2)
elif nd == 0:
    print(0)
else:
    print(-1)
