from collections import defaultdict, deque


def topo_sort(graph):
    lst = []
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            if v in graph:
                in_degree[v] += 1
    s = deque([u for u in graph if in_degree[u] == 0])
    while s:
        lst.append(n := s.popleft())
        for m in graph.get(n, []):
            in_degree[m] -= 1
            if in_degree[m] == 0:
                s.append(m)
    cnt = 0
    for i in in_degree.values():
        if i>0:
            cnt += 1

    return cnt


e = {}
for _ in range(int(input())):
    u, m, *lst = map(int, input().split())
    e[u]=[]
    for v in lst:
        e[u].append(v)
rst=topo_sort(e)
if rst:
    print(rst)
else:
    print("YES")
