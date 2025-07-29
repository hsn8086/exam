import math
from collections import deque


def get(matrix: list[list[int]], start: int):
    w, h = len(matrix[0]), len(matrix)
    if 2 * start >= min(w, h):
        return 0
    que = deque()

    que.extend(matrix[start][start : w - start])
    que.extend(matrix[i][w - start - 1] for i in range(start + 1, h - start))
    que.extend(reversed(matrix[h - start - 1][start : w - start - 1]))
    que.extend(matrix[i][start] for i in range(h - start - 2, start, -1))

    nums = "".join(map(str, que))
    nums = nums + nums
    return sum(1 for i in range(len(que)) if nums[i : i + 4] == "1543")


ntc = int(input())
for _ in range(ntc):
    h, w = map(int, input().split())
    matrix = [list(map(int, input())) for i in range(h)]
    count = 0
    for i in range(math.ceil(min(w, h) / 2)):
        count += get(matrix, i)
    print(count)
