class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        dp = [0]

        for i, d in enumerate(questions[::-1], 1):
            p, bp = d
            dp.append(max(dp[i - 1], dp[max(0, i - bp - 1)] + p))

        return dp[-1]
