import math


def pre(n):
    pri = []
    not_prime = [False] * (n + 1)
    for i in range(2, n + 1):
        if not not_prime[i]:
            pri.append(i)
        for pri_j in pri:
            if i * pri_j > n:
                break
            not_prime[i * pri_j] = True
            if i % pri_j == 0:
                break
    return pri


def break_down(n, pri):
    for pri_j in pri:
        if n % pri_j == 0:
            yield pri_j
            while n % pri_j == 0:
                n //= pri_j
    if n > 1:
        yield n


MOD = 998244353
MAX_VALUE = 10**6 + 10

pri = pre(MAX_VALUE)
n = int(input())
a = list(map(int, input().split()))

sum_lst = [0] * MAX_VALUE
dp = [0] * n

for i in range(0, n):
    ai = a[i]
    now_fac = list(break_down(ai, pri))

    if i == 0:
        dp[i] = 1
        print("init",dp[i])
    else:
        for fac in now_fac:
            dp[i] = (dp[i] + sum_lst[fac]) % MOD

    for fac in now_fac:
        print(fac,i,dp[i])
        sum_lst[fac] = (sum_lst[fac] + dp[i]) % MOD
print(sum_lst[:10])
print(dp)
print(dp[n - 1])
