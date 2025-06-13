
n, m = map(int, input().split())
e = []
for _ in range(m):
    u, v = map(int, input().split())
    e.append((u - 1, v - 1))
if n <= 6:
    print(m)
else:
    ans = 0
    for i in range(n):
        for j in range(i):
            vis = set()
            for u, v in e:
                if u == i:
                    u = j
                if v == i:
                    v = j
                vis.add(tuple(sorted((u, v))))
            ans = max(ans, len(vis))
    print(ans)
