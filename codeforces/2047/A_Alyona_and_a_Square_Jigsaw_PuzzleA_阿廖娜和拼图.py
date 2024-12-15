ntc = int(input())
for _ in range(ntc):
    n = int(input())
    a = map(int, input().split())
    count = 0
    now = 0
    now_red = max(now * 4, 1)
    last = 0
    for v in a:
        if now_red == 0:
            now += 2
            now_red = max(now * 4, 1)
        v = v + last

        if v == now_red:
            v = 0
            now_red = 0
            count += 1
            continue
        while v > 0:
            if v > now_red:
                v -= now_red
                now += 2
                now_red = max(now * 4, 1)
            elif v < now_red:
                now_red -= v
                v = 0
            else:
                v = 0
                now_red = 0
                count += 1
                continue

        last = v
    print(count)
