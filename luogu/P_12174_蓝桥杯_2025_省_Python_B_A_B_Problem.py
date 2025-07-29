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
    
def count_factor_pairs_with_primes(n, pri):
    # 初始化结果数组
    counts = [0] * (n + 1)
    counts[1] = 1  # 1只有1×1这一种
    
    # 初始化最小质因子数组
    min_prime = [0] * (n + 1)
    for p in pri:
        if p > n:
            break
        min_prime[p] = p
    
    # 筛法预处理最小质因子
    for p in pri:
        if p > n:
            break
        for multiple in range(p * 2, n + 1, p):
            if min_prime[multiple] == 0:
                min_prime[multiple] = p
    
    # 计算每个数的因子对数
    for k in range(2, n + 1):
        if min_prime[k] == k:  # k是质数
            counts[k] = 1  # 只有1×k
        else:
            # 质因数分解
            factors = {}
            num = k
            while num > 1:
                p = min_prime[num]
                factors[p] = factors.get(p, 0) + 1
                num = num // p
            
            # 计算因子总数
            total_factors = 1
            for exp in factors.values():
                total_factors *= (exp + 1)
            
            # 因子对数 = ceil(total_factors / 2)
            counts[k] = (total_factors + 1)
    
    return counts[1:] # 返回1到n的结果

n=int(input())
pri = euler_sieve(n)

result = count_factor_pairs_with_primes(n, pri)
print(result)

"""(2, 2), (3, 2), (4, 3), (5, 2), (6, 4), (7, 2), (8, 4), (9, 3), (10, 4), (11, 2), (12, 6), (13, 2), (14, 4), (15, 4), (16, 5), (17, 2), (18, 6), (19, 2), (20, 6), (21, 4), (22, 4), (23, 2), (24, 8), (25, 3), (26, 4), """