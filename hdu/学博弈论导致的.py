from functools import lru_cache

@lru_cache(maxsize=None)
def G(r, b, m):
    if r == 0 and b == 0 and m == 0:
        return 0  # 游戏结束，Grundy数为0
    moves = set()
    # 操作1：拿走k块红宝石
    for k in range(1, 4):
        if r >= k:
            moves.add(G(r - k, b, m))
    # 操作2：把一块蓝宝石变成红宝石
    if b >= 1:
        moves.add(G(r + 1, b - 1, m))
    # 操作3：拿走1块蓝宝石，然后拿走0或1块红宝石
    if b >= 1:
        for k in range(0, 2):
            if r >= k:
                moves.add(G(r - k, b - 1, m))
    # 操作4：拿走2块蓝宝石，然后出现1块红宝石
    if b >= 2:
        moves.add(G(r + 1, b - 2, m))
    # 操作5：拿走一个宝盒说“蓝星”，然后出现1块蓝宝石
    if m >= 1:
        moves.add(G(r, b + 1, m - 1))
    # 操作6：拿走一个宝盒说“赤石”，然后出现1块红宝石
    if m >= 1:
        moves.add(G(r + 1, b, m - 1))
    # 操作7：拿走一个宝盒说“共生”，然后出现1块红宝石和1块蓝宝石
    if m >= 1:
        moves.add(G(r + 1, b + 1, m - 1))
    # 计算mex
    mex = 0
    while mex in moves:
        mex += 1
    return mex

for _ in range(int(input())):
    print("Alice" if G(*map(int,input().split()))!=0 else "Bob")
