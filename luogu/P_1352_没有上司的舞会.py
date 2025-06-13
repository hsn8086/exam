from collections import defaultdict, deque

n = int(input())
r = [0] + [int(input()) for _ in range(n)] # 1base

# build graph
e = defaultdict(list)
s_l = set()
s_all = set(range(1, n + 1))
for _ in range(n - 1):
    l, k = map(int, input().split())
    e[k].append(l)
    s_l.add(l)

root = (s_l ^ s_all).pop() # get root

# bfs get depth
info = [(0, root)]
queue = deque()
queue.append((0, root))
while queue:
    deep, u = queue.popleft()
    for v in e[u]:
        queue.append((deep + 1, v))
        info.append((deep + 1, v))
info.sort(reverse=True)

# dp
dp = [(0, 0)] + [[0, 0] for i in range(1, n + 1)]
for _, u in info:
    for v in e[u]:
        dp[u][0] += max(dp[v][0], dp[v][1])
        dp[u][1] += dp[v][0]
    dp[u][1] += r[u]

print(max(dp[root][0], dp[root][1]))
