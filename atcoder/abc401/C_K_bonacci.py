MOD = 10**9
n, k = map(int, input().split())

dp = [1] * k
prefix = list(range(k + 1))
for _ in range(n - k + 1):
    dp.append((prefix[-1] - prefix[-k - 1]) % MOD)
    prefix.append((prefix[-1] + dp[-1]) % MOD)
print(dp[-1])
