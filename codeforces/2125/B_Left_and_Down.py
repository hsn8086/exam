from math import gcd

for _ in range(int(input())):
    a, b, k = map(int, input().split())
    g = gcd(a, b)
    if a == b or (a // g <= k and b // g <= k):
        print(1)
    else:
        print(2)
