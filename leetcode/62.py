class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] + [0] * (n - 1)
        for i in range(m):
            now = [0]
            for j in range(n):
                now.append(now[-1] + dp[j])
            dp = now[1:]

        return dp[-1]
