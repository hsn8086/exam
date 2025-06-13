for _ in range(int(input())):
    n, x = map(int, input().split())
    a = "".join(input().split())
    idx_l = a.find("1")
    idx_r = a.rfind("1")
    # print(a)
    # print(idx_l,idx_r)
    if idx_l == -1:
        print("YES")
    else:
        if idx_r - idx_l < x:
            print("YES")
        else:
            print("NO")
