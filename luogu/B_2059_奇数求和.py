n, m = map(int, input().split())
ans = 0
for i in range(n, m + 1):
    if i & 1:
        ans += i
print(ans)
