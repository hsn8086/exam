from math import gcd

n, m, k = map(int, input().split())

g = gcd(n, m)

while k:
    if n % g == 0 and m % g == 0:
        k -= 1
    g -= 1
print(g + 1)
