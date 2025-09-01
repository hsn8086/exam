n, c = map(int, input().split())
a = [0] * 35
b = [0] * 35
ans = float("inf")
sum_ = [0, 0, 0]

for i in range(1, n + 1):
    a[i], b[i] = map(int, input().split())


def dfs(x):
    global ans, sum_
    if sum_[1] + sum_[2] >= c:
        ans = min(ans, abs(sum_[1] - sum_[2]))
    if x > n:
        return False
    if ans == 0:
        return True
    sum_[1] += a[x]
    sum_[2] += b[x]
    if dfs(x + 1):
        return True
    sum_[1] -= a[x]
    sum_[2] -= b[x]
    if dfs(x + 1):
        return True
    return False


dfs(1)
if ans != float("inf"):
    print(ans)
else:
    print(-1)
