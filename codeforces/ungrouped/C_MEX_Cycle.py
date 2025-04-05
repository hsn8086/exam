from itertools import cycle

for _ in range(int(input())):
    n, x, y = map(int, input().split())
    a = []
    for i in range(n):

        lst = []
        if a:
            lst.append(a[i - 1])
        if i == y - 1:
            lst.append(a[x - 1])
        if i == n - 1:
            lst.append(0)
        e = 0
        while True:
            if e not in lst:
                a.append(e)
                break
            e += 1

    print(*a)
