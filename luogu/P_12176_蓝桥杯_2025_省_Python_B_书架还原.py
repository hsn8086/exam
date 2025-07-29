def clac(a: list, s: int, vis: set):
    sc = s
    cnt = 0
    while True:
        vis.add(sc)
        sc = a[sc - 1]
        if s == sc:
            break
        cnt += 1
    return cnt


n = int(input())
a = list(map(int, input().split()))
vis = set()
cnt = 0
for i in range(1, n):
    if i not in vis:
        cnt += clac(a, i, vis)

print(cnt)
