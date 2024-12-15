from collections import defaultdict
from collections.abc import Mapping
import heapq


def dijkstra(e: Mapping, s: int) -> Mapping:
    dis = defaultdict(lambda: float("inf"))
    dis[s] = 0
    queue = [(0, s)]
    visited = set()
    while queue:
        _, u = heapq.heappop(queue)
        if u in visited:
            continue
        visited.add(u)
        for v, w in e[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(queue, (dis[v], v))
    return dis


n, m = map(int, input().split())
point = [0] + list(map(int, input().split()))
edges = defaultdict(list)

for _ in range(m):
    u, v, w = map(int, input().split())
    edges[u].append((v, w + point[v]))
    edges[v].append((u, w + point[u]))


dis = dijkstra(edges, 1)
dis[1] = point[1]
rst = map(lambda x: str(x + point[1]), (dis[i] for i in range(2, n + 1)))
print(" ".join(rst))
