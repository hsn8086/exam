xb, yb, xm, ym = map(int, input().split())

men={}
def dfs(x, y, end_x, end_y, blocks):
    if (x,y) in men:
        return men[(x,y)]
    if x > end_x or y > end_y:
        return 0

    if (x, y) in blocks:
        return 0

    if x == end_x and y == end_y:
        return 1

    men[(x,y)]=dfs(x + 1, y, end_x, end_y, blocks) + dfs(x, y + 1, end_x, end_y, blocks)
    return men[(x,y)]

blocks = [
    (xm + 2, ym + 1),
    (xm + 1, ym + 2),
    (xm + 2, ym - 1),
    (xm + 1, ym - 2),
    (xm - 2, ym + 1),
    (xm - 1, ym + 2),
    (xm - 2, ym - 1),
    (xm - 1, ym - 2),
    (xm, ym),
]


print(dfs(0, 0, xb, yb, blocks))
