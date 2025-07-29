for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    c, d, e, f = a[::2], a[1::2], b[::2], b[1::2]
    if f.count("0") >= c.count("1") and e.count("0") >= d.count("1"):
        print("YES")
    else:
        print("NO")
