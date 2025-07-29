for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()),reverse=True)
    count, height = 0, 0
    while k > 0:
        v = (a[-1] - height) * len(a)
        if k > v:
            k -= v; count += v; height = a[-1]
            while a[-1] == height: count += 1; a.pop()
        else:
            count += k; k = 0
    print(count)
