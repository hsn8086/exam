for _ in range(int(input())):
    n, k = map(int, input().split())
    cnt = 0
    rst = []
    r = 0
    while n > 1:
        if cnt | k == k:
            rst.append(cnt)
            r |= cnt
            cnt += 1
            n -= 1
        else:
            while n > 1:
                rst.append(0)
                n -= 1
            break
    if (cnt) | r == k:
        rst.append(cnt)
    else:
        rst.append(r ^ k)

    print(*rst)
