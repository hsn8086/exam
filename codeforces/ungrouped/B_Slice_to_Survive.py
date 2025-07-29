from math import ceil


def check(x, y):
    cnt = 0
    while x > 1:
        x = ceil(x / 2)
        cnt += 1
    while y > 1:
        y = ceil(y / 2)
        cnt += 1
    return cnt


for _ in range(int(input())):
    n, m, a, b = map(int, input().split())
    print(min(check(n, min(b, m - b + 1)), check(min(a, n - a + 1), m)) + 1)
