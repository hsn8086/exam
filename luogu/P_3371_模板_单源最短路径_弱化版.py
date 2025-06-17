from collections import defaultdict
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(e, s):
    vis = set()
    queue = [(0, s)]
    dis = defaultdict(lambda: 2**31 - 1)
    dis[s] = 0
    while queue:
        _, u = heappop(queue)
        if u in vis:
            continue
        vis.add(u)

        for v, w in e[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heappush(queue, (dis[v], v))

    return dis


n, m, s = map(int, input().split())
e = defaultdict(list)
for i in range(m):
    u, v, w = map(int, input().split())
    e[u].append((v, w))

dis = dijkstra(e, s)
print(*(dis[i] for i in range(1, n + 1)))
