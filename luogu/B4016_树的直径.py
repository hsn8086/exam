from collections import deque

n = int(input())
e = [[] for _ in range(n + 1)]
for _ in range(n - 1):  # 读入
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)

visited = bytearray(n + 1)
queue = deque([1])
f = [[] for _ in range(n + 1)]  # 有向树
sorted_node = []  # 拓扑排序
while queue:  # 从根节点出发遍历, 建立有向树和排序
    u = queue.popleft()
    visited[u] = 1
    sorted_node.append(u)
    for v in e[u]:
        if visited[v]:
            continue
        queue.append(v)
        f[u].append(v)

ans = [1] * (n + 1)  # 所有子树的直径
dp = [1] * (n + 1)  # 深度
for u in reversed(sorted_node):
    child = sorted(dp[v] for v in f[u])
    if child:
        dp[u] = child[-1] + 1
    if len(child) >= 2:
        ans[u] = child[-1] + child[-2]

print(max(ans))
