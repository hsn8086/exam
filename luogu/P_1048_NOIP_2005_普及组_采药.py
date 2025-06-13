n, m = map(int, input().split())
dp = [0] * (n + 1)

for i in range(m):
    w, v = map(int, input().split())
    for j in range(n, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)
print(dp[n])
