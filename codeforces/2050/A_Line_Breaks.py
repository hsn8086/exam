t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    words = [input() for _ in range(n)]

    total_len = 0
    ans = 0

    for i in range(n):
        if total_len + len(words[i]) <= m:
            total_len += len(words[i])
            ans += 1
        else:
            break

    print(ans)
