cnt = 0
a = list(map(int, input()))
if len(a) == 1:
    print(a[0] + 1)
else:
    for i, j in zip(a[:-1], a[1:]):
        cnt += (i - j) % 10
    cnt += j

    print(cnt + len(a))
