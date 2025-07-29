from collections import defaultdict

h, w, n = map(int, input().split())

info = []
lx, ly = defaultdict(list), defaultdict(list)
for _ in range(n):
    x, y = map(int, input().split())
    info.append(False)
    lx[x].append(len(info) - 1)
    ly[y].append(len(info) - 1)

for _ in range(int(input())):
    cmd, q = map(int, input().split())
    opl = lx if cmd == 1 else ly
    cnt = 0
    for i in opl[q]:
        if not info[i]:
            info[i] = True
            cnt += 1
    opl.pop(q)
    print(cnt)
