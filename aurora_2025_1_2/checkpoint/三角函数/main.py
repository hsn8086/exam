from math import gcd

for _ in range(int(input())):
    a, _, c = sorted(map(int, input().split()))
    d = gcd(a, c)
    print(f"{a // d}/{c // d}")
