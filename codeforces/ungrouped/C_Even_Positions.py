for _ in range(int(input())):
    cnt = 0
    n = int(input())
    ans = 0
    for i in input():
        if i == "_" and cnt == 0:
            cnt += 1
        elif i == "_" and cnt > 0:
            # print((cnt-1)*2+1)
            ans += (cnt - 1) * 2 + 1
            cnt -= 1
        elif i == "(":
            cnt += 1
        elif i == ")":
            # print()
            ans += (cnt - 1) * 2 + 1
            cnt -= 1
    print(ans)
