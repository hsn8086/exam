def get_min_changes(a: str, b: str, c: str) -> int:
    n, m = len(a), len(b)
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(n + 1):
        for j in range(m + 1):
            if i + j == 0:
                continue
            curr_pos = i + j - 1
            if i > 0:
                cost = 0 if a[i-1] == c[curr_pos] else 1
                dp[i][j] = min(dp[i][j], dp[i-1][j] + cost)
            
            if j > 0:
                cost = 0 if b[j-1] == c[curr_pos] else 1
                dp[i][j] = min(dp[i][j], dp[i][j-1] + cost)
    
    return dp[n][m]


ntc = int(input())
for _ in range(ntc):
    a = input()
    b = input()
    c = input()
    print(get_min_changes(a, b, c))



