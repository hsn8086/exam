for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    c, d = min(c - a, d - b), max(c - a, d - b)
    a, b = min(a, b), max(a, b)

    # print(_)
    # print(a,b,c,d)
    # print((a+1)*2<b,(c+1)*2,d)
    if (a + 1) * 2 < b or (c + 1) * 2 < d:
        print("NO")
    else:
        print("YES")
