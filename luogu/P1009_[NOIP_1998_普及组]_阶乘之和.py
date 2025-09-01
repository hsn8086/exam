from itertools import zip_longest


def carry(a: list):
    for i in range(len(a) - 1):
        div, mod = divmod(a[i], 10)
        a[i + 1] += div
        a[i] = mod
    while not a[-1]:
        a.pop(-1)
    return a


def mul(a: list, b: list):
    length = ((a[-1] + 1) * (b[-1] + 1) >= 10) + len(a) + len(b) - 1
    rst = [0] * (length + 1)

    for i, u in enumerate(a):
        for j, v in enumerate(b):
            rst[i + j] += u * v

    return carry(rst)


def add(a: list, b: list):
    rst = []
    for i, j in zip_longest(a, b, fillvalue=0):
        rst.append(i + j)
    return carry(rst)


rst = []
last = [1]
for i in range(1, int(input()) + 1):
    last = mul(last, [i])
    rst = add(rst, last)
print("".join(map(str, reversed(rst))))
