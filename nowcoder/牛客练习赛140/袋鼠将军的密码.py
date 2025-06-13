for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input()
    if m > n:
        print(-1)
    else:
        print(a[:m])
