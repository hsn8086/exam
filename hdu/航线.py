from collections import defaultdict
import heapq


def dijkstra(e, s):
    vis = set()
    queue = [(0, s)]
    dis = defaultdict(lambda: float("+inf"))
    dis[s] = 0
    while queue:
        _, u = heapq.heappop(queue)
        if u in vis:
            continue
        vis.add(u)
        for v, w in e[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(queue, (dis[v], v))
    return dis


for _ in range(int(input())):
    n, m = map(int, input().split())
    if n == 1 and m == 1:
        print(int(input()) * 2)
        input()
        continue
    e = defaultdict(list)
    fd = -1
    for i in range(n):  # 行
        for j, v in enumerate(map(int, input().split())):
            if fd == -1:
                fd = v
            if j < m - 1:
                e[(i, j + 1, 3)].append(((i, j, 3), v))
            if i < n - 1:
                e[(i + 1, j, 0)].append(((i, j, 0), v))
            if i > 0:
                e[(i - 1, j, 2)].append(((i, j, 2), v))
            if j > 0:
                e[(i, j - 1, 1)].append(((i, j, 1), v))
    for i in range(n):
        for j, v in enumerate(map(int, input().split())):
            e[(i, j, 0)].append(((i, j, 1), v))
            e[(i, j, 0)].append(((i, j, 4), v))
            e[(i, j, 1)].append(((i, j, 2), v))
            e[(i, j, 1)].append(((i, j, 0), v))
            e[(i, j, 2)].append(((i, j, 3), v))
            e[(i, j, 2)].append(((i, j, 1), v))
            e[(i, j, 3)].append(((i, j, 4), v))
            e[(i, j, 3)].append(((i, j, 2), v))
            e[(i, j, 4)].append(((i, j, 1), v))
            e[(i, j, 4)].append(((i, j, 3), v))

    dis = dijkstra(e, (0, 0, 0))

    print(min(dijkstra(e, (0, 0, 0))[n - 1, m - 1, i] + fd for i in range(4)))
