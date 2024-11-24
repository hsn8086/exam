def select(blocks, idx):
    i = idx
    while i > 0:
        if i not in blocks:
            return i
        i -= 1

    return 0


def solve(num_of_q, points, b, current=0, blocks: set = None):
    if not blocks:
        blocks = set()
    blocks.add(current)

    # c
    s1 = select(blocks, current)
    if s1:
        res1 = solve(num_of_q, points, b, current=s1, blocks=blocks)
    else:
        res1 = 0
    # uc
    s2 = select(blocks, b[current] - 1)
    if s2:
        res2 = solve(num_of_q, points, b, current=s2, blocks=blocks)
    else:
        res2 = 0
    if res1 == res2 == 0:
        return points[current]
    return max(res1 + points[current], res2)


num_of_tc = int(input())
for _ in range(num_of_tc):
    num_of_q = int(input())
    points = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(num_of_q, points, b))
