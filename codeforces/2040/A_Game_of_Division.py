def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        can_win = True
        for j in range(n):
            if i == j:
                continue
            if abs(a[i] - a[j]) % k == 0:
                can_win = False
                break
        if can_win:
            print("YES")
            print(i + 1) 
            return
    print("NO")


# 读取测试用例数量
t = int(input())
for _ in range(t):
    solve()
