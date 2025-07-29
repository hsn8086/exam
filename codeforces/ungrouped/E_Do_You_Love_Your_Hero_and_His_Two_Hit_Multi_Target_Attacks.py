from math import sqrt


def newton_method(f, fd, x0, eps=1e-10, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < eps:
            return x
        x = x - fx / fd(x)
    return x


for _ in range(int(input())):
    n = int(input())
    fl = int(
        newton_method(
            f=lambda x: ((1 + x) * x) / 2 - n,
            fd=lambda x: (x + 1) / 2,
            x0=sqrt(2 * n),
        )
    )
    addl = int(n - ((1 + fl) * fl) / 2)

    print(fl + addl * 2)
    for i in range(fl):
        print(0, i + 10)
    for i in range(addl):
        print((i + 1) * 2, -(i + 1) * 2)
        print((i + 1) * 2 + 1, -(i + 1) * 2)
