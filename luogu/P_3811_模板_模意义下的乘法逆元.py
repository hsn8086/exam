import sys


# def extended_gcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = extended_gcd(b % a, a)
#         return (g, x - (b // a) * y, y)


# def mod_inverse(a, m):
#     g, x, y = extended_gcd(a, m)
#     if g != 1:
#         return None  # 逆元不存在
#     else:
#         return x % m
sys.stdout = sys.__stdout__
input = sys.stdin.readline

n, m = map(int, input().split())


print(1)

inv = [1] * (n + 1)
for i in range(2, n + 1):
    inv[i] = m - m // i * inv[m % i] % m
    print(inv[i])


# rst = [str(pow(i, -1, m)) for i in range(1, n + 1)]


# sys.stdout.flush()
