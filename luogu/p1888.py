import math


a, b, c = map(int, input().split())

max_ = max(a, b, c)
min_ = min(a, b, c)

g = math.gcd(max_, min_)
print(f"{min_//g}/{max_//g}")
