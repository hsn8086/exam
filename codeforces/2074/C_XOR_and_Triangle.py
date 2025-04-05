for _ in range(int(input())):
    x = int(input())
    if (x & (x - 1)) == 0 or ((x + 1) & x) == 0:
        print(-1)
        continue

    s = r = 0
    for i in range(30):
        if (x & (1 << i)) == 0 and s == 0:
            s = 1 << i
        if (x & (1 << i)) != 0 and r == 0:
            r = 1 << i
        if s and r:
            break

    print(s + r)
