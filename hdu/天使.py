from math import comb


MOD = 10**9 + 7
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    sum_ = 0
    for i in a:
        ans += sum_ * i
        sum_ += i
        ans %= MOD

    comb_cnt = 1
    for i in range(2, n + 1):
        comb_cnt *= comb(i, 2) % MOD
    print(ans % MOD, comb_cnt % MOD)
