for _ in range(int(input())):
    n, k = map(int, input().split())
    k = max(k, 1)
    a = list(map(int, input().split()))
    a.sort()
    print(a[-k] - a[k - 1] + 1)
