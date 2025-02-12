for _ in range(int(input())):
    n, m, k = map(int, input().split())
    if max(n - m, m - n) > k or max(n,m)<k:
        print(-1)
        continue

    flag = n > m

    while n > 0 or m > 0:
        if flag:
            if n >= k:
                n -= k
                print("0" * k, end="")
            else:
                print("0" * n, end="")
                n = 0
        else:
            if m >= k:
                m -= k
                print("1" * k, end="")
            else:
                print("1" * m, end="")
                m = 0
        flag = not flag
    print()
