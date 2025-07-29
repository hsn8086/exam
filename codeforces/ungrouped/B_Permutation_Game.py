from itertools import pairwise

n, m = map(int, input().split())
a = list(map(int, input().split()))
start_i = a[0]
lst = [0] * n
used = set()
for i, j in pairwise(a):
    now = (j + n - i - 1) % n + 1
    if (lst[start_i - 1] and lst[start_i - 1] != now) or (
        lst[start_i - 1] != now and now in used
    ):
        print(-1)
        break
    used.add(now)
    lst[start_i - 1] = now
    start_i = (now + start_i) % n
else:
    su = used ^ set(range(1, n + 1))

    for i in range(len(lst)):
        if lst[i] == 0:
            lst[i] = su.pop()
    print(*lst)

[].copy