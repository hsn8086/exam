import sys
lst = [0] * 10010
for inp in sys.stdin:
    if not inp.strip():
        continue
    left, h, right = map(int, inp.strip().split())
    for i in range(left, right):
        lst[i] = max(lst[i], h)
res = []


for i in range(1, len(lst)):
    if lst[i - 1] != lst[i]:
        res.append(i)
        res.append(lst[i])


print(" ".join(map(str, res)))

#     lst.append(tuple(map(int, inp.split())))

# lst.sort(key=lambda e: e[0])

# res = []

# lr = 0
# lh = 0
# for i in lst:
#     left, h, right = i
#     if left > lr:
#         res.append(lr)
#         res.append(0)

#     if h > lh:
#         res.append(left)
#         res.append(h)

#     lr = right
