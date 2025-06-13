from math import ceil

a, b = map(int, input().split())

print(min(ceil(a / b), a // b, key=lambda x: abs(x - a / b)))
