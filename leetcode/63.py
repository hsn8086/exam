class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        dp = [1] + [0] * (len(obstacleGrid[0]) - 1)
        for line in obstacleGrid:
            now = [0]
            for i, v in enumerate(line):
                now.append(0 if v else now[-1] + dp[i])
            dp = now[1:]
        return dp[-1]
