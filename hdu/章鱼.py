from collections import defaultdict


def dfs(e, vis, i):
    if vis[i]:
        return 0
    vis[i] = 1
    ans = 0
    for j in e[i]:
        dfs(e, vis, j)
        ans+=vis[j]
    vis[i] += ans
    

for _ in range(int(input())):
    n = int(input())
    e = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        e[u].append(v)
        e[v].append(u)
    tag=[0] * (n + 1)
    dfs(e, tag, 1)
    print(tag)