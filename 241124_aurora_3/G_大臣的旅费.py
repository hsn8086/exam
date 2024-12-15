import sys

sys.setrecursionlimit(10010)

MAX_N = 10010

nodes_count = 0
farthest_node = 0
distance = [0] * MAX_N
graph = [[] for _ in range(MAX_N)]


def find_farthest_node(current, parent):
    global farthest_node
    for neighbor, weight in graph[current]:
        if neighbor == parent:
            continue
        distance[neighbor] = distance[current] + weight
        if distance[neighbor] > distance[farthest_node]:
            farthest_node = neighbor
        find_farthest_node(neighbor, current)


nodes_count = int(input())

for _ in range(nodes_count - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


find_farthest_node(1, 0)

distance[farthest_node] = 0
find_farthest_node(farthest_node, 0)


print(distance[farthest_node])
