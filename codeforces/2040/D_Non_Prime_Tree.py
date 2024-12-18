import sys


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        tree[u].append(v)
        tree[v].append(u)
    depth = [0] * (n + 1)
    from collections import deque

    queue = deque()
    queue.append(1)
    depth[1] = 1
    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if depth[neighbor] == 0:
                depth[neighbor] = depth[node] + 1
                queue.append(neighbor)
    group1 = []
    group2 = []
    for i in range(1, n + 1):
        if depth[i] % 2 == 1:
            group1.append(i)
        else:
            group2.append(i)
    assigned = [0] * (n + 1)
    num1 = 1
    for node in group1:
        assigned[node] = num1
        num1 += 2
    num2 = 2
    for node in group2:
        assigned[node] = num2
        num2 += 2
    print(" ".join(map(str, assigned[1:])))
