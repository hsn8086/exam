import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def max_acyclic_subgraph(graph, n):
    visited = [False] * (n + 1)
    in_stack = [False] * (n + 1)
    cycle_edges = 0

    def dfs(node, parent):
        nonlocal cycle_edges
        visited[node] = True
        in_stack[node] = True

        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    pass
            elif in_stack[neighbor] and neighbor != parent:
                cycle_edges += 1

        in_stack[node] = False
        return False

    for node in graph:
        if not visited[node]:
            dfs(node, -1)

    return cycle_edges


n, m = map(int, input().split())
e = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)
print(max_acyclic_subgraph(e, n))
