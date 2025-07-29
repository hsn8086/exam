import sys

input = sys.stdin.readline


n, q = map(int, input().split())
d, c = [0], [0]
for _ in range(n):
    a, b = map(int, input().split())
    d.append(a)
    c.append(b)
LOG = 18
stk = []
nxt = [[0] * (LOG + 1) for _ in range(n + 1)]
sum_ = [[0] * (LOG + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    while stk and d[stk[-1]] < d[i]:
        nxt[stk[-1]][0] = i
        sum_[stk[-1]][0] += c[i]
        stk.pop()
    stk.append(i)

while stk:
    nxt[stk[-1]][0] = 0
    stk.pop()
for j in range(1, LOG + 1):
    for i in range(1, n + 1):
        if nxt[i][j - 1] != 0:
            nxt[i][j] = nxt[nxt[i][j - 1]][j - 1]
            sum_[i][j] = sum_[i][j - 1] + sum_[nxt[i][j - 1]][j - 1]
        else:
            nxt[i][j] = 0
            sum_[i][j] = 0
for _ in range(q):
    r, v = map(int, input().split())
    if c[r] >= v:
        print(r)
        continue

    v -= c[r]
    current = r

    for i in range(LOG, -1, -1):
        if nxt[current][i] != 0 and v > sum_[current][i]:
            v -= sum_[current][i]
            current = nxt[current][i]

    print(nxt[current][0] if nxt[current][0] != 0 else 0)
