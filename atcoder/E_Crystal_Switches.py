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


# def bfs01(e, s):
#     vis = set()
#     queue = deque([(0, s)])
#     dis = defaultdict(lambda: float("+inf"))
#     dis[s] = 0
#     while queue:
#         _, u = queue.popleft()
#         if u in vis:
#             continue
#         vis.add(u)
#         for v, w in e[u]:
#             if dis[v] > dis[u] + w:
#                 dis[v] = dis[u] + w
#                 if w == 0:
#                     queue.appendleft((dis[v], v))
#                 else:
#                     queue.append((dis[v], v))
#     return dis


e = defaultdict(list)
n, m, k = map(int, input().split())
for i in range(m):
    u, v, w = map(int, input().split())
    e[(u, w)].append(((v, w), 1))
    e[(v, w)].append(((u, w), 1))

for i in map(int, input().split()):
    e[(i, 1)].append(((i, 0), 0))
    e[(i, 0)].append(((i, 1), 0))

dis = dijkstra(e, (1, 1))
rst = min(dis[(n, 1)], dis[(n, 0)])
print(-1 if rst >= float("+inf") else rst)
