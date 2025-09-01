import heapq
import sys

input = sys.stdin.readline


def dijkstra(e, s, n):
    INF = 0
    queue = [(-1, s)]
    dis = [INF] * (n + 1)
    dis[s] = 1
    while queue:
        d, u = heapq.heappop(queue)
        d = -d
        if d < dis[u]:
            continue

        for v, w in e[u]:
            if dis[v] < dis[u] * w:
                dis[v] = dis[u] * w
                heapq.heappush(queue, (-dis[v], v))
    return dis


n, m = map(int, input().split())
e = [[] for _ in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    e[u].append((v, 1 - w / 100))
    e[v].append((u, 1 - w / 100))


a, b = map(int, input().split())
dis = dijkstra(e, a, n)
print(f"{100 / dis[b]:0.8f}")
