n = int(input(), 2)
b = [0, 1, 1]
for i in range(3, 10**7):
    b.append(b[i // 2] + (i & 1))

dp = [1] * (64)
for i in range(2, 64):
    dp[i] = dp[i - 1] + dp[i - 2]
cnt = 0
for i in range(1, n + 1):
    cnt = (cnt + dp[b[i] - 1]) % (10**9 + 7)
print(cnt)
# dp = [1] * (n.bit_count() + 10)
# for i in range(2, n.bit_count() + 1):
#     dp[i] = dp[i - 1] + dp[i - 2]
# cnt = 0

# for i in range(1, n + 1):
#     cnt += dp[i.bit_count() - 1] % (10**9 + 7)

# print(cnt % (10**9 + 7))
