# from collections import defaultdict
# from heapq import heappop, heappush
# import sys
# input = sys.stdin.readline

# def dijkstra(e, s):
#     vis = set()
#     queue = [(0, s)]
#     dis = defaultdict(lambda: 2**31 - 1)
#     dis[s] = 0
#     while queue:
#         _, u = heappop(queue)
#         if u in vis:
#             continue
#         vis.add(u)

#         for v, w in e[u]:
#             if dis[v] > dis[u] + w:
#                 dis[v] = dis[u] + w
#                 heappush(queue, (dis[v], v))

#     return dis


# n, m, s = map(int, input().split())
# e = defaultdict(list)
# for i in range(m):
#     u, v, w = map(int, input().split())
#     e[u].append((v, w))

# dis = dijkstra(e, s)
# print(*(dis[i] for i in range(1, n + 1)))


def bellman_ford(e, s, n):
    INF = 1 << 70
    dis = [INF] * (n + 1)
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


n, m, s = map(int, input().split())
e = [[] for _ in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    e[u].append((v, w))

dis = bellman_ford(e, s, n)
print(*(dis[1:]))
