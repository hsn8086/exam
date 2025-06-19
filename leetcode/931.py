inf = 1 << 70


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        dp = [0] * (len(matrix[0]) + 2)
        for line in matrix:
            now = []
            for i, v in enumerate(line, 1):
                now.append(min(dp[i - 1], dp[i], dp[i + 1]) + v)
            dp = [inf] + now + [inf]
        return min(dp)
