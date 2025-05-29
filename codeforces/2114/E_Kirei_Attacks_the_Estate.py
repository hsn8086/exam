import sys
from collections import defaultdict, deque

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    w_lst = [0] + list(map(int, input().split()))

    e = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        e[u].append(v)
        e[v].append(u)

    levels = []
    parent = [1] * (n + 1)
    queue = deque()
    queue.append((1, 0, 1))
    # build
    used = set()
    while queue:
        u, level, par = queue.popleft()
        if u in used:
            continue
        used.add(u)
        parent[u] = par
        # print(u)
        if len(levels) <= level:
            levels.append([])

        levels[level].append(u)

        for v in e[u]:
            queue.append((v, level + 1, u))

    # print(parent)
    # clac
    max_dp = [w_lst[1]] * (n + 1)
    min_dp = [w_lst[1]] * (n + 1)
    for i, lev in enumerate(levels[1:]):
        for u in lev:
            # print(u, parent[u])
            max_dp[u] = max(w_lst[u], w_lst[u] - min_dp[parent[u]])
            min_dp[u] = min(w_lst[u], w_lst[u] - max_dp[parent[u]])
    print(*max_dp[1:])
    # print(min_dp)
