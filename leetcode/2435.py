class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        dp = [[0] * k for i in range(len(grid[0]))]
        dp[0][0] = 1
        for line in grid:
            now = [[0] * k]
            for i, v in enumerate(line):
                tba = [0] * k
                for n in range(k):
                    tba[(n + v) % k] = dp[i][n] + now[-1][n]
                now.append(tba)
            dp = now[1:]
        return dp[-1][0] % (10**9 + 7)
