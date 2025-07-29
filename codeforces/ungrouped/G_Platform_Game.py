import sys
from bisect import bisect_left

input = sys.stdin.readline


def query(level, x):
    level_ = list(map(lambda t: t[0], level))
    idx = bisect_left(level_, x)
    return idx


if __name__ == "__main__":
    for _ in range(int(input())):
        mp = []
        for _ in range(int(input())):
            mp.append(tuple(map(int, input().split())))

        sx, sy = map(int, input().split())

        mp.sort(key=lambda t: (-t[2], t[0]))

        mp2 = []
        last_y = -1
        lst = []
        for l, r, y in mp:
            if y > sy:
                continue
            if last_y == y:
                lst.append((l, r))
            else:
                if lst:
                    mp2.append(lst)
                lst = [(l, r)]
                last_y = y
        if lst:
            mp2.append(lst)
        for lev in mp2:
            idx = query(lev, sx)
            l, r = lev[idx - 1]

            if l < sx < r:
                sx = r
        print(sx)
