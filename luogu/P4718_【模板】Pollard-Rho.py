import math
import random


def brent_pollard_rho(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5

    if is_prime(n):
        return n

    y, c, m = (
        random.randint(1, n - 1),
        random.randint(1, n - 1),
        random.randint(1, n - 1),
    )
    g, r, q = 1, 1, 1

    while g == 1:
        x = y
        for i in range(r):
            y = (pow(y, 2, n) + c) % n

        k = 0
        while k < r and g == 1:
            ys = y
            for i in range(min(m, r - k)):
                y = (pow(y, 2, n) + c) % n
                q = q * abs(x - y) % n

            g = math.gcd(q, n)
            k += m

        r *= 2

    if g == n:
        while True:
            ys = (pow(ys, 2, n) + c) % n
            g = math.gcd(abs(x - ys), n)
            if g > 1:
                break

    return g


def is_prime(n):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# def factorize(n):
#     if n == 1:
#         return []
#     if is_prime(n):
#         return [n]

#     divisor = brent_pollard_rho(n)
#     return factorize(divisor) + factorize(n // divisor)


for _ in range(int(input())):
    n = int(input())
    if is_prime(n):
        print("Prime")
    else:
        print(brent_pollard_rho(n))