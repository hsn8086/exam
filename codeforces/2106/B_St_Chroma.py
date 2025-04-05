for _ in range(int(input())):
    n, k = map(int, input().split())
    rst = []
    rst.extend(range(k))
    rst.extend(range(n - 1, k - 1, -1))
    print(*rst)
