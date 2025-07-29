import sys


def fast_input():
    return sys.stdin.readline().strip()


N = 2 * 10**5 + 5
A = 10**6 + 5
MOD = 998244353


n = 0
a = [0] * N
cnt = 0
p = [0] * A
f = [0] * N
g = [0] * A
flg = [False] * A

fc = [[] for _ in range(A)]


def euler_sieve():
    global cnt

    for i in range(2, A):
        if not flg[i]:
            cnt += 1
            p[cnt] = i
            fc[i].append(i)

        for j in range(1, cnt + 1):
            v = i * p[j]

            if v >= A:
                break

            flg[v] = True

            fc[v] = fc[i].copy()

            if i % p[j] != 0:
                fc[v].append(p[j])
            else:
                break


def calc(x):
    factors = fc[x]
    c = len(factors)
    res = []

    for i in range(1, 1 << c):
        product = 1
        num_factors_in_subset = 0

        for j in range(c):
            if (i >> j) & 1:
                product *= factors[j]
                num_factors_in_subset += 1

        sign = 1 if num_factors_in_subset % 2 == 1 else -1
        res.append(sign * product)
    return res


euler_sieve()

n = int(fast_input())

input_line = list(map(int, fast_input().split()))
for i in range(n):
    a[i + 1] = input_line[i]

for i in range(1, n + 1):
    tmp = calc(a[i])

    if i == 1:
        f[i] = 1
    else:
        current_f = 0
        for t in tmp:
            x = abs(t)
            y = 1 if t > 0 else -1

            term = (y * g[x]) % MOD
            current_f = (current_f + term + MOD) % MOD
        f[i] = current_f

    for t in tmp:
        x = abs(t)
        g[x] = (g[x] + f[i]) % MOD

print(f[n])
