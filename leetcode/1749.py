inf = 10**20


class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        ans = 0
        dp = -inf
        for i in nums:
            dp = max(dp + i, i)
            ans = max(ans, dp)

        dp = inf
        for i in nums:
            dp = min(dp + i, i)
            ans = max(ans, -dp)
        return ans
