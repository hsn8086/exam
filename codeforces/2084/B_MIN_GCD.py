# import random
# from math import gcd


# def pollards_rho(n):
#     if n % 2 == 0:
#         return 2
#     if n % 3 == 0:
#         return 3
#     if n % 5 == 0:
#         return 5

#     while True:
#         # 随机选择初始值
#         c = random.randint(2, n - 1)
#         f = lambda x: (pow(x, 2, n) + c) % n
#         x, y, d = 2, 2, 1

#         while d == 1:
#             x = f(x)
#             y = f(f(y))
#             d = gcd((x - y) % n, n)

#         if d != n:
#             return d


# def factor(n):
#     factors = []

#     def _factor(n):
#         if n == 1:
#             return
#         if is_prime(n):
#             factors.append(n)
#             return

#         d = pollards_rho(n)
#         if d is None:
#             factors.append(n)
#             return

#         _factor(d)
#         _factor(n // d)

#     _factor(n)
#     return factors


# def is_prime(n, k=5):
#     if n <= 1:
#         return False
#     elif n <= 3:
#         return True
#     elif n % 2 == 0:
#         return False

#     d = n - 1
#     s = 0
#     while d % 2 == 0:
#         d //= 2
#         s += 1

#     for _ in range(k):
#         a = random.randint(2, n - 2)
#         x = pow(a, d, n)
#         if x == 1 or x == n - 1:
#             continue

#         for __ in range(s - 1):
#             x = pow(x, 2, n)
#             if x == n - 1:
#                 break
#         else:
#             return False
#     return True


# for _ in range(int(input())):
#     n = int(input())
#     a = sorted(map(int, input().split()))
#     target = a[0]
#     if a[0] == a[1]:
#         print("Yes")
#         continue
#     a.pop(0)

#     lst = None
#     for i in a:
#         fac = factor(i)
#         if target in fac:
#             if not lst:
#                 lst = fac
#             else:
#                 common = []
#                 len1, len2 = len(lst), len(fac)
#                 j, k = 0, 0
#                 while j < len1 and k < len2:
#                     if lst[j] == fac[k]:
#                         common.append(lst[j])
#                         k += 1
#                         j += 1
#                     elif lst[j] < fac[k]:
#                         j += 1
#                     else:
#                         k += 1
#                 lst = common

#     if lst and len(lst) == 1:
#         print("Yes")
#     else:
#         print("No")
from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    target = a.pop(0)
    lst = list(filter(lambda i: gcd(i, target) == target, a))
    if gcd(*lst) == target:
        print("Yes")
    else:
        print("No")
