import itertools
import sys


def solve(square: int, x1: int, x2: int, y1: int, y2: int):
    down = square[x1 - 2][y2 - 1] if x1 - 2 >= 0 and y2 - 1 >= 0 else 0
    right = square[x2 - 1][y1 - 2] if x2 - 1 >= 0 and y1 - 2 >= 0 else 0
    center = square[x1 - 2][y1 - 2] if x1 - 2 >= 0 and y1 - 2 >= 0 else 0
    return square[x2 - 1][y2 - 1] - down - right + center


def square_gen(n):
    for i in range(n):
        yield map(int, input().split())


n = int(input())
if n == 0:
    print(0)
    sys.exit(0)

qsquare = []
for i, lst in enumerate(square_gen(n)):
    rt_lst = []
    for j, e in enumerate(lst):
        last = rt_lst[-1] if rt_lst else 0
        recent = qsquare[-1][j] if qsquare else 0
        recent_last = (
            qsquare[-1][j - 1] if qsquare and qsquare[-1] and j - 1 >= 0 else 0
        )
        rt_lst.append(e + last + recent - recent_last)
    qsquare.append(rt_lst)
max_ = float("-inf")
for x1, y1 in itertools.product(range(1, n + 1), range(1, n + 1)):
    for x2, y2 in itertools.product(range(x1, n + 1), range(y1, n + 1)):
        rst = solve(qsquare, x1, x2, y1, y2)
        if rst > max_:
            max_ = rst
print(max_)
