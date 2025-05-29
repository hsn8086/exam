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


pri_prefix = [0]
for i in euler_sieve(6 * 10**6):
    pri_prefix.append(pri_prefix[-1] + i)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    # print(a)
    a_prefix = [0]
    for i in a:
        a_prefix.append(a_prefix[-1] + i)
    # print(*a_prefix)
    # print(*pri_prefix[:6])
    for i in range(1, n + 1):
        if a_prefix[i] < pri_prefix[i]:
            print(n - i + 1)
            break

    else:
        print(0)
