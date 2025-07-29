for _ in range(int(input())):
    n, m = map(int, input().split())
    s = set()
    t = 0
    for _ in range(n):
        p, q = map(int, input().split())
        s.add(t)
        t += p * (48 // q)

    cnt = 0
    t = 0
    for _ in range(m):
        p, q = map(int, input().split())
        if t in s:
            cnt += 1
        t += p * (48 // q)
    print(cnt)
