import sys
from itertools import product
from functools import cache

sys.setrecursionlimit(114514)

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

moves_x = [-1, 0, 1, 0]
moves_y = [0, -1, 0, 1]

mem = [[0] * m for _ in range(n)]


def search(x: int, y: int):
    if mem[x][y]:
        return mem[x][y]
    ans = 1
    for dx, dy in zip(moves_x, moves_y):
        if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m:
            continue
        if matrix[x + dx][y + dy] < matrix[x][y]:
            ans = max(ans, search(x + dx, y + dy) + 1)
    mem[x][y] = ans
    return ans


ans = 0
for x, y in product(range(n), range(m)):
    ans = max(ans, search(x, y))

print(ans)
