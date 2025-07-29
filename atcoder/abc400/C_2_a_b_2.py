import math

n = int(input())
cnt = 0
max_ = int(math.isqrt(n) + 10)
for k in range(1, max_ + 1, 2):
    m = n // (k**2)
    if m >= 2:
        cnt += m.bit_length() - 1
print(cnt)
