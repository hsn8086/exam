class Solution:
    def minPathCost(self, grid: list[list[int]], moveCost: list[list[int]]) -> int:
        dp = grid[0]

        for j, line in enumerate(grid[1:], 1):
            now = []
            for i, v in enumerate(line):
                now.append(
                    min(m + moveCost[grid[j - 1][n]][i] for n, m in enumerate(dp)) + v
                )
            dp = now
        return min(dp)
