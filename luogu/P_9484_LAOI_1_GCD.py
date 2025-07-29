from math import gcd, lcm

for _ in range(int(input())):
    n, q = map(int, input().split())
    f = [[float("+inf") for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        f[i][i] = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if x % y == 0 or y % x == 0:
                w = abs(x - y)
                f[x][y] = min(w, f[x][y])
                f[y][x] = min(w, f[y][x])

    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                f[x][y] = min(f[x][y], f[x][k] + f[k][y])

    for _ in range(q):
        x, y = map(int, input().split())
        print(f[x][y])
