n, m = map(int, input().split())

n += 1
m += 1

mv = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(x, y, vis):
    if x < 1 or y < 1 or x > n or y > m or vis[x][y]:
        return 0
    elif x == 1 or y == 1 or x == n or y == m:
        return 1
    
    vis[x][y] = 1
    ans = sum(dfs(x + dx, y + dy, vis) for dx, dy in mv)
    vis[x][y] = 0
    
    return ans


vis = [bytearray(m + 1) for _ in range(n + 1)]
ans = 0
for i in range(2, n):
    vis[i][1] = 1
    ans += dfs(i, 2, vis)
    vis[i][1] = 0

for i in range(2, m):
    vis[1][i] = 1
    ans += dfs(2, i, vis)
    vis[1][i] = 0


print(ans)
