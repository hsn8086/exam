
def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val]

# Precompute primes up to 10^5; adjust limit if needed.
primes = sieve(100000)

semi_prime_cache = {}
def is_semi_prime(n):
    if n in semi_prime_cache:
        return semi_prime_cache[n]
    cnt = 0
    temp = n
    for p in primes:
        if p * p > temp:
            break
        while temp % p == 0:
            cnt += 1
            temp //= p
            if cnt > 2:
                semi_prime_cache[n] = False
                return False
        if temp == 1:
            break
    if temp > 1:
        cnt += 1
    semi_prime_cache[n] = (cnt == 2)
    return semi_prime_cache[n]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    lcm_cache = {}
    for i in range(n):
        for j in range(i, n):
            # Using tuple (min, max) to cache results for given pair
            key = (min(a[i], a[j]), max(a[i], a[j]))
            if key in lcm_cache:
                l = lcm_cache[key]
            else:
                l = lcm(a[i], a[j])
                lcm_cache[key] = l
            if is_semi_prime(l):
                count += 1
    
    print(count)