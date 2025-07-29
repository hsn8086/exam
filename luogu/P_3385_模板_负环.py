INF = 1 << 70


def bellman_ford(e, s, n):
    dis = [INF] * (n + 2)
    dis[s] = 0
    for _ in range(n):
        updated = False
        for u in range(1, n + 1):
            for v, w in e[u]:
                if dis[u] < INF and dis[v] > dis[u] + w:
                    dis[v] = dis[u] + w
                    updated = True
        if not updated:
            break
    else:
        return None
    return dis


import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    e = [[] for _ in range(n + 2)]

    for i in range(m):
        u, v, w = map(int, input().split())
        if w >= 0:
            e[u].append((v, w))
            e[v].append((u, w))
        else:
            e[u].append((v, w))

    rst = bellman_ford(e, 1, n)

    print("YES" if rst is None else "NO")
