import sys


def num_reader():
    cache = 0
    flag = False
    while chunk := sys.stdin.buffer.read(1 << 16):
        for byte in chunk:
            if 48 <= byte <= 57:
                cache = (cache << 3) + (cache << 1) + byte - 48
                flag = True
                continue

            if flag:
                yield cache 
                cache = 0
                flag = False




mod = (1 << 64) - 1
inp = num_reader()
mp = {}
ans = 0
for i in range(1, next(inp) + 1):
    x, y = next(inp), next(inp)
    ans += i * mp.get(x, 0)
    mp[x] = y
print(ans & mod)
