import sys
sys.set_int_max_str_digits(0)
def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = exgcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return d, x, y

a = int(input())
b = int(input())
mod = 19260817

d, x, y = exgcd(b, mod)
if d != 1:
    print("Angry!")
else:
    inv_b = x % mod
    print((a * inv_b) % mod)
