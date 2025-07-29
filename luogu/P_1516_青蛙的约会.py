from math import gcd, ceil


# (a + bn) % v == 0
def min_n(a: int, b: int, v: int):
    c = (-a) % v
    d = gcd(b, v)
    if c % d != 0: return None
    b1, v1, c1 = b // d, v // d, c // d
    inv = pow(b1, -1, v1)
    return (inv * c1) % v1


x, y, m, n, length = map(int, input().split())

diff, v = x - y, n - m
if m > n: diff, v = -diff, -v

init_n = ceil((max(-diff, 0)) / length)

a = (length * init_n + diff) % v
b = length % v

if (n_diff := min_n(a, b, v)) is not None:
    print(((init_n + n_diff) * length + diff) // v)
else:
    print("Impossible")
