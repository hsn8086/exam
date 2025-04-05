import math

n = int(input())

div, mod = divmod(n, 3)
total = 2 * div
if mod == 2:
    total += 1
    rem = 1
else:
    rem = 2 * mod

total += math.ceil((n + rem) / 2)
print(total)
