from math import sqrt


def f(x, n):
    if n == 1:
        return sqrt(1 + x)
    else:
        return sqrt(n + f(x, n - 1))


x, n = map(float, input().split())

print(f"{f(x, int(n)):0.2f}")
