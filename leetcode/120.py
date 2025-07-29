inf = 1 << 70


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [0, 0]
        for line in triangle:
            now = []
            for i, v in enumerate(line):
                now.append(min(dp[i], dp[i + 1]) + v)
            dp = [inf] + now + [inf]
        return min(dp)
