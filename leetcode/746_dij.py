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


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        e = defaultdict(list)
        e[0].append((1, 0))
        e[0].append((2, 0))
        for i, c in enumerate(cost, 1):
            e[i].append((i + 1, c))
            e[i].append((i + 2, c))

        dis = dijkstra(e, 0)

        return dis[len(cost) + 1]
