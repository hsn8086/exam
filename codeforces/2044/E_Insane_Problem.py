ntc = int(input())
for _ in range(ntc):
    k, l1, r1, l2, r2 = map(int, input().split())
    count = 0
    n = 0
    while True:
        power = pow(k, n)
        if power > r2:
            break
        lower_x = max(l1, (l2 + power - 1) // power)
        upper_x = min(r1, r2 // power)
        if lower_x <= upper_x:
            count += upper_x - lower_x + 1
        n += 1
    print(count)
