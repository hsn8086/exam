inf = 10**20


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [-inf]
        for i in nums:
            dp.append(max(dp[-1] + i, i))
        return max(dp)

