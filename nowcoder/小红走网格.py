from math import gcd

for _ in range(int(input())):
    x, y, a, b, c, d = map(int, input().split())
    # m*a=y+n*b
    x_f = x % gcd(c, d) == 0
    y_f = y % gcd(a, b) == 0
    print("YES" if x_f and y_f else "NO")
