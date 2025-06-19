inf = 1 << 70


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = [0] + ([inf] * (len(grid[0]) - 1))

        for line in grid:
            now = [inf]
            for i, v in enumerate(line):
                now.append(min(now[-1], dp[i]) + v)
            dp = now[1:]

        return dp[-1]



