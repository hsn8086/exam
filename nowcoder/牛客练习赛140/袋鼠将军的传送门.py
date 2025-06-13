for _ in range(int(input())):
    n, t = map(int, input().split())
    now = 1
    cnt = 0
    ans = min(t, cnt + abs(t - now))
    while True:
        now += n // now
        # print(now,cnt)
        ans = min(ans, cnt + abs(t - now))
        if not (t - now > 0 and n // now > 1):
            break
        cnt += 1
    print(ans)
