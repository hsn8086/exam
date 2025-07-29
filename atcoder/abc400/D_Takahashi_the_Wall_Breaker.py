from collections import defaultdict
import heapq


def dijkstra(e, s):
    vis = set()
    queue = [(0, s)]
    dis = defaultdict(lambda: float("+inf"))
    dis[s] = 0
    while queue:
        _, u = heapq.heappop(queue)
        if u in vis:
            continue
        vis.add(u)
        for v, w in e[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(queue, (dis[v], v))
    return dis


def dfs(matrix: list[list[str]], start_xy: tuple, id_: int):
    x, y = start_xy
    h = len(matrix)
    w = len(matrix[0])
    if x > h - 1 or y > w - 1 or x < 0 or y < 0:
        return
    if matrix[x][y] == ".":
        matrix[x][y] = id_
        yield from dfs(matrix, (x + 1, y), id_)
        yield from dfs(matrix, (x - 1, y), id_)
        yield from dfs(matrix, (x, y + 1), id_)
        yield from dfs(matrix, (x, y - 1), id_)
        for x2 in range(-3, 4):
            if x + x2 < 0 or x + x2 > h - 1:
                continue
            for y2 in range(-3, 4):
                if y + y2 < 0 or y + y2 > w - 1:
                    continue
                if (
                    matrix[x + x2][y + y2] != "#"
                    and matrix[x + x2][y + y2] != "."
                    and matrix[x + x2][y + y2] != id_
                ):
                    yield (id_, int(matrix[x + x2][y + y2]))


h, w = map(int, input().split())
matrix = []
for i in range(h):
    matrix.append(list(input()))
e = defaultdict(set)
id_ = 0
for i in range(h):
    for j in range(w):
        if matrix[i][j] == ".":
            id_ += 1
            for u, v in dfs(matrix, (i, j), id_):
                e[u].add((v, 1))
                e[v].add((u, 1))
a, b, c, d = map(int, input().split())
c,d=c-1,d-1
start_id = int(matrix[a - 1][b - 1])
# end_id = int(matrix[c - 1][d - 1])
end_ids = []
for x2 in range(-3, 4):
    if c + x2 < 0 or c + x2 > h - 1:
        continue
    for y2 in range(-3, 4):
        if d + y2 < 0 or d + y2 > w - 1:
            continue
        if matrix[c + x2][d + y2] != "#" and matrix[c + x2][d + y2] != ".":
            end_ids.append(int(matrix[c + x2][d + y2]))
dis = dijkstra(e, start_id)
min_dis = float("+inf")

if matrix[c][d] != "#" and matrix[c][d] != ".":
    min_dis = min(min_dis, dis[int(matrix[c][d])])
for end_id in end_ids:
    min_dis = min(min_dis, dis[end_id] + 1)
print(min_dis)
