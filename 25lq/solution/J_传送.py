from collections import deque

n, m = map(int, input().split())
start_x, start_y = map(int, input().split())
end_x, end_y = map(int, input().split())
matrix = [input().strip() for _ in range(n)]

start_x -= 1
start_y -= 1
end_x -= 1
end_y -= 1


dist = [[float("+inf")] * m for _ in range(n)]
dist[start_x][start_y] = 0
queue = deque()
queue.appendleft((start_x, start_y))

dx_lst = [-1, 1, 0, 0]
dy_lst = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    if x == end_x and y == end_y:
        break

    # 向相邻位置移动
    for dx, dy in zip(dx_lst, dy_lst):
        nx = x + dx
        ny = y + dy
        if (
            0 <= nx < n
            and 0 <= ny < m
            and matrix[nx][ny] == "."
            and dist[nx][ny] > dist[x][y]
        ):
            dist[nx][ny] = dist[x][y]
            queue.appendleft((nx, ny))

    # 使用传送魔法
    for i in range(x - 2, x + 3):
        for j in range(y - 2, y + 3):
            if (
                0 <= i < n
                and 0 <= j < m
                and matrix[i][j] == "."
                and dist[i][j] > dist[x][y] + 1
            ):
                dist[i][j] = dist[x][y] + 1
                queue.append((i, j))

if dist[end_x][end_y] == float("+inf"):
    print(-1)
else:
    print(dist[end_x][end_y])
