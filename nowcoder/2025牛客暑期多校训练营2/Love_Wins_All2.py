import sys
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

MOD = 998244353

def modpow(a, b):
    res = 1
    while b:
        if b & 1:
            res = res * a % MOD
        a = a * a % MOD
        b >>= 1
    return res

def solve(n, a):
    vis = [False] * (n + 1)
    odd_lens, even_lens = [], []

    for i in range(1, n + 1):
        if not vis[i]:
            u = i
            cnt = 0
            while not vis[u]:
                vis[u] = True
                u = a[u]
                cnt += 1
            if cnt % 2 == 1:
                odd_lens.append(cnt)
            else:
                even_lens.append(cnt)

    me = len(even_lens)
    mo = len(odd_lens)
    pow2_me = modpow(2, me)

    ans = 0

    # 情况1：两个未婚在同一个偶环，其他环要能匹配完（即没有奇环）
    if mo == 0:
        sum_f2 = 0
        for L in even_lens:
            term = (L // 4) * L
            if L % 4 == 2:
                term += L // 2
            sum_f2 = (sum_f2 + term) % MOD
        coef = pow2_me * modpow(2, MOD - 2) % MOD
        ans = (ans + coef * sum_f2) % MOD

    # 情况2：两个未婚分别来自两个不同奇环
    if mo == 2:
        L1, L2 = odd_lens
        term = L1 * L2 % MOD
        term = term * pow2_me % MOD
        ans = (ans + term) % MOD

    return ans

# 读取所有输入
T = int(input())
results = []
total_n = 0

for _ in range(T):
    n = int(input())
    total_n += n
    a = list(map(int, input().split()))
    a = [0] + a  # 下标从1开始
    results.append(solve(n, a))

print('\n'.join(map(str, results)))
