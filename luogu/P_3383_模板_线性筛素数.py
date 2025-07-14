import sys


def euler_sieve(n):
    pri = []
    not_prime = bytearray(n + 1)
    for i in range(2, n + 1):
        if not not_prime[i]:
            pri.append(i)
        for p in pri:
            if i * p > n:
                break
            not_prime[i * p] = 1
            if i % p == 0:
                break
    return pri


input = sys.stdin.readline
n, q = map(int, input().split())
pri = euler_sieve(n)

queries = [int(sys.stdin.readline()) for _ in range(q)]
for k in queries:
    print(pri[k - 1])
