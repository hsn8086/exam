import sys
from itertools import islice

def fast_read(func=int):
    CHUNK_SIZE = 16384
    cache = bytes()
    while d := sys.stdin.buffer.read(CHUNK_SIZE):
        ds = (cache + d).split()
        del cache
        if d[-1] != 32 and d[-1] != 10:
            cache = ds.pop(-1)
        else:
            cache = bytes()
        yield from map(lambda x: func(x.decode()), ds)
        del ds
    yield func(cache.decode())


inp = fast_read()
n, p = islice(inp, 2)

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
