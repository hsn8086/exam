for _ in range(int(input())):
    n, k = map(int, input().split())
    bits = list(map(int, input()))
    cnt = 0
    flag = False
    for i in bits:
        if i:
            cnt += 1
        else:
            cnt = 0
        if cnt >= k:
            print("NO")
            flag = True
            break
    if flag:
        continue

    print("YES")
    p_lst = []
    n_lst = []
    for i, v in enumerate(bits):
        if v:
            p_lst.append(i)
        else:
            n_lst.append(i)
    rst = [0] * n
    for v, i in enumerate(p_lst + n_lst, start=1):
        rst[i] = v
    print(*rst)
