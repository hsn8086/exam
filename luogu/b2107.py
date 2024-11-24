n, m = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(map(int, input().split())))
for y in range(m):
    print(" ".join(str(g[n - x - 1][y]) for x in range(n)))
