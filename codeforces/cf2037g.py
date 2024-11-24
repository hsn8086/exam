import math
import bisect


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
    factors = set()
    init = n
    i = 0
    while i < len(pri) and pri[i] * pri[i] <= n:
        if n % pri[i] == 0:
            factors.add(pri[i])
            while n % pri[i] == 0:
                n //= pri[i]
        i += 1
    if n > 1:
        factors.add(n)
    return factors


def mapping(n, pri):
    pos = bisect.bisect_left(pri, n)
    if pos == len(pri) or pri[pos] != n:
        return -1
    return pos


pri = pre(10**6+2)

mapi = lambda x: mapping(x, pri)
n = int(input())
a = list(map(int, input().split()))

MAX_PRIME_INDEX = 78500  # 根据10^6的质数个数估算
dp = [[0 for i in range(n)]  for _ in range(MAX_PRIME_INDEX)]

now_pris = break_down(a[0], pri)
for pri_j in now_pris:
    pos = mapi(pri_j)
    if pos != -1:
        dp[pos][0] = 1

for i in range(1, n - 1):
    now_pris = break_down(a[i], pri)

    _sum = 0
    now_pos=[]
    for pri_j in now_pris:
        pos = mapi(pri_j)
        now_pos.append(pos)

    for j in range(i):
        for pos in now_pos:
            if dp[pos][j] > 0:
                _sum += dp[pos][j]
                break

    for pos in now_pos:
        dp[pos][i] = _sum

result = 0
now_pris = break_down(a[-1], pri)
for pri_j in now_pris:
    pos = mapi(pri_j)
    if pos != -1:
        result += sum(dp[pos][:n-1])
print(result)
