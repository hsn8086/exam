from math import sqrt
from itertools import combinations


def clac_line(
    p1: tuple[int, int], p2: tuple[int, int], *, k_reverse: bool = False
) -> tuple[float, float]:
    if k_reverse:
        p1x,p1y=p1
        p2x,p2y=p2
        mid_x=(p1x+p2x)/2
        mid_y=(p1y+p2y)/2
        
        p1=(mid_x,mid_y)
        p2=(p1x,p2y)
        
    if p1[0] == p2[0]:
        return float("inf"), p1[0]

    k = (p1[1] - p2[1]) / (p1[0] - p2[0])
    p = p1
    b = p[1] - k * p[0]
    print(k,b,p1,p2,p,k)
    return k, b


def cacl_circ(
    p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int]
) -> tuple[tuple[int, int], float]:
    l1, l2 = list(
        filter(
            lambda t: t[0] != float("inf"),
            map(lambda t: clac_line(*t, k_reverse=True), combinations([p1, p2, p3], 2)),
        )
    )[:2]
    k1, b1 = l1
    k2, b2 = l2

    x = (b2 - b1) / (k1 - k2)
    y = k1 * x + b1
    r = sqrt((x - p1[0]) ** 2 + (y - p1[1]) ** 2)

    return ((x, y), r)


for _ in range(int(input())):
    p1 = tuple(map(int, input().split()))
    p2 = tuple(map(int, input().split()))
    p3 = tuple(map(int, input().split()))
    p = tuple(map(int, input().split()))
    v = tuple(map(int, input().split()))
    print(cacl_circ(p1, p2, p3))
