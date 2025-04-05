for _ in range(int(input())):
    n, q = map(int, input().split())
    p = [0] + list(map(int, input().split()))

    mp = [0] * (n + 1)
    for i in range(1, n + 1):
        mp[p[i]] = i

    for _ in range(q):
        l, r, x = map(int, input().split())

        px = mp[x]
        if px < l or px > r:
            print(-1, end=" ")
            continue

        cnt_l = cnt_r = 0
        sg = lg = 0

        while True:
            m = (l + r) // 2
            if m == px:
                break
            if m < px:
                cnt_l += 1
                if p[m] < x:
                    sg += 1
                l = m + 1
            else:
                cnt_r += 1
                if p[m] > x:
                    lg += 1
                r = m - 1

        if cnt_l > x - 1 or cnt_r > n - x:
            print(-1, end=" ")
            continue

        d = 2 * max(cnt_l - sg, cnt_r - lg)
        print(d, end=" ")

    print()
