n, m = map(int, input().split())
f = [[float("+inf") for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    f[i][i] = 0
for _ in range(m):
    u, v, w = map(int, input().split())
    f[u][v] = min(w, f[u][v])
    f[v][u] = min(w, f[v][u])

for k in range(1, n + 1):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            f[x][y] = min(f[x][y], f[x][k] + f[k][y])

for x in range(1, n + 1):
    print(*(f[x][y] for y in range(1, n + 1)))
