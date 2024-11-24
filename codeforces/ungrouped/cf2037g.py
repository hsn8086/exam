from math import gcd
from collections import defaultdict
import sys

MOD = 998244353


input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))


dp = [0] * n
dp[0] = 1

next_city = defaultdict(list)
for i in range(n):
    for j in range(i + 1, n):
        if gcd(a[i], a[j]) != 1:
            next_city[j].append(i)


for j in range(1, n):
    for i in next_city[j]:
        dp[j] += dp[i]
        dp[j] %= MOD


print(dp[-1])
