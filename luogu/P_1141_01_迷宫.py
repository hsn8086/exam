from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


def bfs(
    matrix, record_m, record_l, sx, sy, n, last_status, visited: list[list[int]], i
):
    if record_m[sx][sy] != -1:
        return record_l[record_m[sx][sy]]
    queue = deque([(sx, sy, -1)])
    ans = 0
    while queue:
        sx, sy, last_status = queue.popleft()
        if sx >= n or sy >= n or sx < 0 or sy < 0 or last_status == matrix[sx][sy]:
            continue
        if visited[sx][sy] == i:
            continue
        visited[sx][sy] = i
        record_m[sx][sy] = i
        ans += 1
        queue.append((sx + 1, sy, matrix[sx][sy]))
        queue.append((sx - 1, sy, matrix[sx][sy]))
        queue.append((sx, sy + 1, matrix[sx][sy]))
        queue.append((sx, sy - 1, matrix[sx][sy]))

    return ans


n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(input())
visited = [[-1 for _ in range(n)] for _ in range(n)]
record_m = [[-1 for _ in range(n)] for _ in range(n)]
record_l = []
for i in range(m):
    sx, sy = map(int, input().split())
    rst = bfs(matrix, record_m, record_l, sx - 1, sy - 1, n, -1, visited, i)
    record_l.append(rst)
    print(rst)
