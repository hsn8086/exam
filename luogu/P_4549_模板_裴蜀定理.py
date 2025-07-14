from math import gcd

n = int(input())
print(gcd(*map(int, input().split())))
