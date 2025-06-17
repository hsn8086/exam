class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        nums = [zero, one]
        dp = [1] + [0] * (high + max(nums))
        for i in range(high):
            for step in nums:
                dp[i + step] += dp[i]
        return sum(dp[low : high + 1]) % (10**9 + 7)
