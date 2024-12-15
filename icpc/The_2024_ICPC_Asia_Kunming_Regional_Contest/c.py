import sys


def calc0(u, n, k):
    v = min(n, ((u + k - 1) // k) * k)
    up = (u - 1) // k + 1
    u += (v - u) // up * up
    return u


def calc1(u, k):
    v = 0
    while ((u + k - 1) // k) > ((v + k - 1) // k):
        tmp = ((u + k - 1) // k) - ((v + k - 1) // k)
        v = u
        u += tmp
    return u


data = sys.stdin.read().split()
ntc = int(data[0])
ptr = 1
results = []
for _ in range(ntc):
    n, k = int(data[ptr]), int(data[ptr + 1])
    ptr += 2

    u = 1
    while True:
        v = calc0(u, n, k)
        if v <= n:
            u = v
        v = calc1(u, k)
        if v > n:
            break
        u = v
    results.append(str(u))
print("\n".join(results))
