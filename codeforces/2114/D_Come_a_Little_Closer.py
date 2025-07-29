import math

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        for _ in range(n): input().split()
        continue
    if n == 2:
        print(2)
        for _ in range(n): input().split()
        continue

    lst_x = []; lst_y = []; lst = []
    for _ in range(n):
        x, y = map(int, input().split())
        lst_x.append(x); lst_y.append(y); lst.append((x, y))
    lst_x.sort(); lst_y.sort()
    min_spend = math.inf
    for x, y in lst:
        idx_x_l = 0; idx_x_r = n - 1
        idx_y_l = 0; idx_y_r = n - 1
        if lst_x[0] == x:
            idx_x_l = 1
        elif lst_x[-1] == x:
            idx_x_r = n - 2
        if lst_y[0] == y:
            idx_y_l = 1
        elif lst_y[-1] == y:
            idx_y_r = n - 2

        rect_x = lst_x[idx_x_r] - lst_x[idx_x_l] + 1
        rect_y = lst_y[idx_y_r] - lst_y[idx_y_l] + 1

        spend = rect_y * rect_x

        if spend == n - 1: spend += min(rect_x, rect_y)
        min_spend = min(min_spend, spend)
    print(min_spend)
