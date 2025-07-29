ntc = int(input())
for _ in range(ntc):
    x, y, k = map(int, input().split())
    xnn = x // k + (1 if x % k else 0)
    xyn = y // k + (1 if y % k else 0)

    print(max((xnn - 1) * 2 + 1, xyn * 2))
