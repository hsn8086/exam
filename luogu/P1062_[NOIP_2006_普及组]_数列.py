n, k = map(int, input().split())

ans = 0
for i in range(10):
    now = 1 << i
    if now & k:
        ans += n**i

print(ans)
