import sys


sys.set_int_max_str_digits(0)
n, m = map(int, input().split())
rst = 0
for i in range(m + 1):
    rst += n**i
if rst > 10**9:
    print("inf")
else:
    print(rst)
