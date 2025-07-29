from itertools import product


def check_range(l1, r1, l2, r2):
    if r1 < l2 or r2 < l1:
        return False
    return True


n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(input())

lines_x = []
lines_y = []

for line in matrix:
    flag = 0
    start = 0
    end = 0
    for i, c in enumerate(line, 1):
        if flag == 0:
            if c == "B":
                if start == 0:
                    start = i
                end = i
            elif start != 0:
                flag = -1
        elif flag == -1:
            if c == "B":
                print("NO")
                break
    else:
        lines_x.append((start, end))
        continue
    break
else:
    for line in zip(*matrix):
        flag = 0
        start = 0
        end = 0
        for i, c in enumerate(line, 1):
            if flag == 0:
                if c == "B":
                    if start == 0:
                        start = i
                    end = i
                elif start != 0:
                    flag = -1
            elif flag == -1:
                if c == "B":
                    print("NO")
                    break
                    ...
        else:
            lines_y.append((start, end))
            continue
        break
    else:
        # print(lines_x)
        # print(lines_y)
        for y1, lst_1 in enumerate(matrix):
            for x1, c1 in enumerate(lst_1):
                for y2, lst_2 in enumerate(matrix):
                    for x2, c2 in enumerate(lst_2):
                        if c1 == "B" and c2 == "B":
                            # print(x1, y1, x2, y2)
                            if not (
                                (lines_x[y1][0]<=x2+1<=lines_x[y1][1] and lines_y[x2][0]<=y1+1<=lines_y[x2][1])
                                or
                                (lines_x[y2][0]<=x1+1<=lines_x[y2][1] and lines_y[x1][0]<=y2+1<=lines_y[x1][1])
                            ):
                                # print(*lines_x[y1], *lines_y[x2])
                                # print(*lines_x[y2], *lines_y[x1])
                                print("NO")
                                break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            print("YES")
