from collections import defaultdict
import heapq
import sys


def dijkstra(e, s):
    INF = 1 << 70
    queue = [(0, s)]
    dis = defaultdict(lambda: INF)
    dis[s] = 0
    while queue:
        d, u = heapq.heappop(queue)
        if d > dis[u]:
            continue
        for v, w in e[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(queue, (dis[v], v))
    return dis


input = sys.stdin.readline
n, m, s = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
dis = dijkstra(adj, s)
print(*(dis[i] for i in range(1, n + 1)))
