import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    INF = float("inf")
    prefix = [0] * (m + 1)
    i = 0
    for j in range(1, m + 1):
        while i < n and a[i] < b[j - 1]:
            i += 1
        if i < n:
            prefix[j] = i + 1
            i += 1
        else:
            prefix[j] = INF

    if prefix[m] <= n:
        print(0)
        continue

    shuf = [0] * (m + 2)
    shuf[m + 1] = n + 1
    i = n - 1
    for j in range(m, 0, -1):
        while i >= 0 and a[i] < b[j - 1]:
            i -= 1
        if i >= 0:
            shuf[j] = i + 1
            i -= 1
        else:
            shuf[j] = 0

    ans = float("inf")
    for p in range(1, m + 1):
        if prefix[p - 1] < shuf[p + 1]:
            ans = min(ans, b[p - 1])

    print(ans if ans < float("inf") else -1)
