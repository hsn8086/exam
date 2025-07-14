from random import randint
from collections import defaultdict, deque
import heapq


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


def bellman_ford(e, s, n):
    INF = 1 << 70
    dis = defaultdict(lambda: INF)
    dis[s] = 0
    for _ in range(n):
        updated = False
        for u in e:
            for v, w in e[u]:
                if dis[u] < INF and dis[v] > dis[u] + w:
                    dis[v] = dis[u] + w
                    updated = True
        if not updated:
            break
    else:
        return None
    return dis

def johnson(e, nodes):
    virtual_node = hex(randint(1 << (4 * 4), 1 << (5 * 4)))
    e[virtual_node] = [(node, 0) for node in nodes]

    h = bellman_ford(e, virtual_node,len((nodes)))
    if h is None:
        return None

    new_edges = defaultdict(list)
    for u in e:
        for v, w in e[u]:
            new_edges[u].append((v, w + h[u] - h[v]))

    result = defaultdict(lambda: defaultdict(lambda: float("+inf")))
    for u in nodes:
        dist = dijkstra(new_edges, u)
        result[u].update({v: dist[v] - h[u] + h[v] for v in dist if v != virtual_node})

    return result

e = defaultdict(list)
points = set()
n, m = map(int, input().split())
for i in range(m):
    a, b, t = input().split()
    e[a].append((b, int(t)))
    points.add(a)
    points.add(b)


dis = johnson(e, points)

for i in range(int(input())):
    a, b = input().split()
    if dis[a][b] < float("+inf"):
        print(dis[a][b])
    else:
        print("Roger")