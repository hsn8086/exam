from itertools import product

n, m = map(int, input().split())

squa_sum = 0
rect_sum = 0
for x, y in product(range(1, n + 1), range(1, m + 1)):
    squa_sum += max(min(x, y), 0)
    rect_sum += x * y

print(squa_sum, rect_sum - squa_sum)
