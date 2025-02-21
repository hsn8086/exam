from collections.abc import Generator
import sys


def chunk_reader(func=int, chunk_size=1 << 15) -> Generator[int, None, None]:
    inp_cache = ""
    while True:
        chunk = sys.stdin.read(chunk_size)
        if not chunk:
            if inp_cache:
                yield func(inp_cache)
                del inp_cache
            break

        for c in chunk:
            if c.isspace():
                if inp_cache:
                    yield func(inp_cache)
                    del inp_cache
                    inp_cache = ""
            else:
                inp_cache += c
            del c
        del chunk


inp = chunk_reader()
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
