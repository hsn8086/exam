import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    q = int(input())
    size = 1 << n
    for __ in range(q):
        query, qc = input().split(maxsplit=1)
        if query == "->":
            x, y = map(int, qc.split())
            res = 0
            k = n
            cx, cy = x - 1, y - 1
            for step in range(n, 0, -1):
                half = 1 << (step - 1)
                quadrant = 0
                if cx < half and cy < half:
                    quadrant = 0
                elif cx >= half and cy >= half:
                    quadrant = 1
                elif cx >= half and cy < half:
                    quadrant = 2
                else:
                    quadrant = 3
                res += quadrant * (1 << (2 * step - 2))
                cx %= half
                cy %= half
            if cx == 0 and cy == 0:
                res += 1
            elif cx == 1 and cy == 1:
                res += 2
            elif cx == 1 and cy == 0:
                res += 3
            elif cx == 0 and cy == 1:
                res += 4
            print(res)
        elif query == "<-":
            d = int(qc)
            d0 = d - 1
            x, y = 0, 0
            for step in range(n, 0, -1):
                half = 1 << (step - 1)
                quadrant_size = 1 << (2 * step - 2)
                quadrant = d0 // quadrant_size
                d0 %= quadrant_size
                if quadrant == 0:
                    pass
                elif quadrant == 1:
                    x += half
                    y += half
                elif quadrant == 2:
                    x += half
                elif quadrant == 3:
                    y += half

            if d0 == 0:
                x += 1
                y += 1
            elif d0 == 1:
                x += 2
                y += 2
            elif d0 == 2:
                x += 2
                y += 1
            elif d0 == 3:
                x += 1
                y += 2
            print(x, y)
