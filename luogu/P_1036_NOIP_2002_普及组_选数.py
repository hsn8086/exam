from itertools import combinations


def euler(n=0):
    prime = []
    not_prime = [False] * (n + 1)

    for i in range(2, n + 1):
        if not not_prime[i]:
            prime.append(i)

        for pri in prime:
            if i * pri > n:
                break
            not_prime[i * pri] = True
            if i % pri == 0:
                break
    return prime


pri = set(euler(10**6))
n, k = map(int, input().split())
a = map(int, input().split())
cnt = 0
for nums in combinations(a, r=k):
    if sum(nums) in pri:
        cnt += 1
print(cnt)
