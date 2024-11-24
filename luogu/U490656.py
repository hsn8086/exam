def solve(square: int, x1: int, x2: int, y1: int, y2: int):
    down = square[x1 - 2][y2 - 1] if x1 - 2 >= 0 and y2 - 1 >= 0 else 0
    right = square[x2 - 1][y1 - 2] if x2 - 1 >= 0 and y1 - 2 >= 0 else 0
    center = square[x1 - 2][y1 - 2] if x1 - 2 >= 0 and y1 - 2 >= 0 else 0
    return square[x2 - 1][y2 - 1] - down - right + center


def square_gen(n):
    for i in range(n):
        yield map(int, input().split())


n, m, q = map(int, input().split())


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

for i in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print(solve(qsquare, x1, x2, y1, y2))
