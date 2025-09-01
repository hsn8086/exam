import sys
from itertools import product

sys.setrecursionlimit(114514)


def dfs(matrix, x, y, n, id_val):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif matrix[x][y] == 1 or matrix[x][y] == id_val:
        return True
    matrix[x][y] = id_val

    return all(dfs(matrix, x + dx, y + dy, n, id_val) for dx, dy in moves)


moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))


s = set()
for i, d in enumerate(product(range(n), repeat=2), 3):
    x, y = d
    if matrix[x][y] == 0 and dfs(matrix, x, y, n, i):
        s.add(i)

for row in matrix:
    for i, e in enumerate(row):
        if e in s:
            row[i] = 2
        elif e != 1:
            row[i] = 0
for row in matrix:
    print(*row)
