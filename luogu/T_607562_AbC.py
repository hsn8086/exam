def euler_sieve(n):
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


n = int(input())
pri = euler_sieve(10**6)

cnt = set()
for a in range(0, len(pri)):
    for b in range(a + 1, len(pri)):
        for c in range(b + 1, len(pri)):
            if (pri[a] ** 2) * pri[b] * (pri[c] ** 2) <= n:
                cnt.add((pri[a] ** 2) * pri[b] * (pri[c] ** 2))
            else:
                break
        if (pri[a] ** 2) * pri[b] * 1 > n:
            break
    if (pri[a] ** 2) * 1 * 1 > n:
        break


print(len(cnt))
