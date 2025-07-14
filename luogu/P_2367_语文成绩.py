import sys


def num_reader():
    cache = 0
    flag = False
    neg = False
    while chunk := sys.stdin.buffer.read(1<<16):
        for byte in chunk:
            if 48 <= byte <= 57:
                cache = (cache << 3) + (cache << 1) + byte - 48
                flag = True
                continue

            if flag:
                yield -cache if neg else cache
                cache = 0
                flag = False
                neg = False

            if byte == 45:
                neg = True


inp = num_reader()

n, p = next(inp), next(inp)

a = [next(inp) for _ in range(n)]
dif = [0 for _ in range(n + 1)]
for _ in range(p):
    x, y, z = next(inp), next(inp), next(inp)
    dif[x - 1] += z
    dif[y] -= z

for i in range(1, n):
    dif[i] += dif[i - 1]

m = min(ai + di for ai, di in zip(a, dif))
print(m)
