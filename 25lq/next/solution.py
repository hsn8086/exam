
import sys

sys.setrecursionlimit(114514)


def check(start: int, end: int, k: int) -> tuple[int, int]:
    if end - start + 1 < k:
        return 0, 0

    mid = (start + end) >> 1
    luck = mid if (start - end + 1) & 1 == 1 else 0

    l_rst, l_luck_point = check(start, mid + (-1 if luck else 0), k)
    r_rst = l_rst + mid * l_luck_point

    return (
        l_rst + r_rst + luck,
        2 * l_luck_point + (1 if luck else 0),
    )


for _ in range(int(input())):
    n, k = map(int, input().split())
    print(check(1, n, k)[0])
