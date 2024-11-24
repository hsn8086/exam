import math


def solve(x, y, k):
    min_ = min(x, y)
    offset = k**2 - min_**2
    if offset <= 0:
        yield f"0 0 {k} 0"
        yield f"0 0 0 {k}"
    else:
        sqof=math.ceil(math.sqrt(offset))
        if x > y:
            yield f"0 0 {sqof} {y}"
            yield f"0 {y} {y} {y-sqof}"
        else:
            yield f"0 0 {x} {sqof}"
            yield f"{x} 0 {x-sqof} {x}"


num_of_tc = int(input())
for _ in range(num_of_tc):
    x, y, k = map(int, input().split())

    for i in solve(x, y, k):
        print(i)
