
def is_divisor(a, b):
    return b != 0 and a % b == 0

n = int(input())

for _ in range(n):
    x, m = map(int, input().split())
    count = 0

    for y in range(1, min(m + 1, x + 1)):
        xor = x ^ y
        if is_divisor(xor, x) or is_divisor(xor, y):
            count += 1

    xor = x
    while xor <= (1 << (len(bin(m)) - 2)):
        xor += x
        y = x ^ xor
        if y <= m and y != 0:
            count += 1

    print(count)