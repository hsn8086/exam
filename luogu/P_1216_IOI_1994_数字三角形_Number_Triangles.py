dp = []
for _ in range(int(input())):
    a = map(int, input().split())
    if not dp:
        dp = list(a)
        continue
    tmp = []
    for i, v in enumerate(a):
        if i == 0:
            tmp.append(dp[0] + v)
        elif i == len(dp):
            tmp.append(dp[-1] + v)
        else:
            tmp.append(max(dp[i - 1] + v, dp[i] + v))
    dp = tmp
print(max(dp))
