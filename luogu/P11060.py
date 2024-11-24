import math

n = int(input())
print("YES" if (math.factorial(n) % (n + 1) == 0) else "NO")
