import heapq
from collections import defaultdict


def dijk(adj, s):
    dis = defaultdict(lambda: float("+inf"))
    dis[s] = 0
    queue = [(0, s)]
    visted = set()
    while queue:
        _, u = heapq.heappop(queue)
        if u in visted:
            continue

        for v, w in adj[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(queue, (dis[v], v))
    return dis

n,m,s=map(int,input().split())
adj=defaultdict(list)
for _ in range(m):
    u,v,w=map(int,input().split())
    adj[u].append((v,w))
dis=dijk(adj,s)
for i in range(1,n+1):
    print(dis[i],end=" ")
print()