from collections import defaultdict, deque
import heapq
import sys
sys.setrecursionlimit(114514)

def dfs(e, s, visited: list):
    if visited[s]:
        return
    visited[s] = True
    print(s, end=" ")

    for i in e[s]:
        dfs(e, i, visited)

    return


def bfs(e, s):
    q = deque([s])
    visited = [False] * len(e)
    while q:
        point = q.popleft()
        print(point, end=" ")
        for i in e[point]:
            if visited[i]:
                continue
            visited[i] = True
            q.append(i)

    return


n, m = map(int, input().split())
e = [list() for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    e[u].append(v)
for lst in e:
    lst.sort()

dfs(e, 1, [False] * len(e))
print()
bfs(e, 1)
# print(*dfs(e, 1, d_vis))
# d_vis.clear()
# print(*bfs(e, 1))
