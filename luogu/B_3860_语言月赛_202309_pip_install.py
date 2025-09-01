from collections import defaultdict, deque

graph = defaultdict(list)
for i in range(1, int(input()) + 1):
    _, *lst = map(int, input().split())
    graph[i].extend(lst)

deq = deque()
deq.append(1)
vis = set()
while deq:
    now = deq.pop()
    if now in vis:
        continue
    vis.add(now)

    for v in graph[now]:
        deq.append(v)

print(len(vis))
