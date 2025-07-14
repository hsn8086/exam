from array import array
import sys


def num_reader():
    cache = 0
    flag = False
    while d := sys.stdin.buffer.read(1 << 32):
        for i in d:
            if i < 48 or i > 57:
                if flag:
                    yield cache
                cache = 0
                flag = False
            else:
                flag = True
                cache *= 10
                cache += i - 48
    if flag:
        yield cache


inp = num_reader()
n = next(inp)
a = array("I", [0]) * n
for i in range(n):
    a[i] = next(inp)

rec = array("I", [0]) * n
stk = array("I", [0]) * n
top = 0

for i in range(n):
    while top > 0 and a[stk[top - 1]] < a[i]:
        rec[stk[top - 1]] = i + 1
        top -= 1
    stk[top] = i
    top += 1

for i in range(n):
    sys.stdout.write(str(rec[i]) + " ")
