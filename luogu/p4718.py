
import math
import random


def pollard_rho(n, rt=0):
    if n % 2 == 0:
        return 2  # 如果n是偶数，直接返回2

    # 定义轮转函数
    def f(x, c):
        return (x * x + c) % n

    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1

    while d == 1:
        x = f(x, c)
        y = f(f(y, c), c)
        d = math.gcd(abs(x - y), n)
        if d == n:
            if rt > 5:
                return d
            return pollard_rho(n, rt=rt + 1)  # 如果失败，重新尝试

    return d


ntc = int(input())
for _ in range(ntc):
    num = int(input())
    print(pollard_rho(num))