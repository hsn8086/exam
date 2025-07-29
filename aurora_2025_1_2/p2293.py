import sys

sys.set_int_max_str_digits(10001)
n = int(input())
x = int(input())
l = 0
r = 1
while r**n <= x:
    l, r = r, r * 2

while l + 1 < r:
    mid = (l + r) // 2
    if mid**n <= x:
        l = mid
    else:
        r = mid


print(l)
