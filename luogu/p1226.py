a, b, p = map(int, input().split())
original_a = a
original_b = b
res = 1
a %= p
while b > 0:
    if b % 2 == 1:
        res = res * a % p
    a = a * a % p
    b //= 2
print(f"{original_a}^{original_b} mod {p}={res}")