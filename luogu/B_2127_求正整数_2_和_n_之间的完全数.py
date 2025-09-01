n = int(input())
for i in range(2, n + 1):
    ans = 0
    for j in range(1, i):
        if not i % j:
            ans += j
    if ans == i:
        print(ans)
        