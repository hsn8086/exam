from bisect import bisect_left


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


pri = euler_sieve(10**5)
for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print("2 1")
        continue
    if n == 3:
        print("2 1 3")
        continue
    rst = []
    idx = bisect_left(pri, n // 2)
    if pri[idx] > n // 2:
        idx -= 1
    target = pri[idx]

    for i in range(1, target + 1):
        rst.append(i)
        rst.append(target * 2 - i)
    if rst[-1] == rst[-2]:
        rst.pop()
    rst = rst[::-1]
    for i in range(target * 2, n + 1):
        rst.append(i)
    print(*rst)

