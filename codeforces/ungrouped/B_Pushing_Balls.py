for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = [list(map(int, input())) for _ in range(n)]

    dp_left = [[False for _ in range(m)] for _ in range(n)]
    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] == 0:
                break
            dp_left[i][j] = True

    dp_top = [[False for _ in range(m)] for _ in range(n)]
    for j in range(0, m):
        for i in range(0, n):
            if matrix[i][j] == 0:
                break
            dp_top[i][j] = True

    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] and (not (dp_left[i][j] or dp_top[i][j])):
                print("NO")
                break
        else:
            continue
        break
    else:
        print("YES")
