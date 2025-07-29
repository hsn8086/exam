for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    max_p = (0, 0)
    max_v = 0
    for i in range(n):
        now = 0
        for j, v in enumerate(a[i + 1 :]):
            if v < a[i]:
                now += 1
            elif v > a[i]:
                now -= 1

            if max_v < now:
                max_p = (i, j + i + 1)
                max_v = now

    print(*map(lambda x: x + 1, max_p))
