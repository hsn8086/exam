for _ in range(int(input())):
    n = int(input())
    matrix = [[0 for i in range(n)] for j in range(n)]

    dx, dy = 1, 0
    x, y = 0, 0
    for i in range(n**2 - 1, -1, -1):
        matrix[x][y] = i
        if not 0 <= x + dx < n or not 0 <= y + dy < n or matrix[x + dx][y + dy]:
            dx, dy = -dy, dx
        x, y = x + dx, y + dy

    for line in matrix:
        print(*line)
