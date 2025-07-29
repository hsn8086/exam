import bisect


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


MAX_PRI = 10000100
# MAX_PRI = 10000
pri = euler_sieve(MAX_PRI)


def get(n):
    global pri
    num_of_pri = bisect.bisect(pri, n, hi=min(n + 1, len(pri)))
    return num_of_pri


for _ in range(int(input())):
    n = int(input())
    cnt=0
    for i in range(1,n+1):
        v=n//i
        if v<2:
            break
        cnt+=get(v)
    print(cnt)
