class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        dp_p = nums[0]
        dp_n = nums[0]
        ans = nums[0]
        for i in nums[1:]:
            dp_p, dp_n = max(dp_n * i, dp_p * i, i), min(dp_n * i, dp_p * i, i)
            ans = max(ans, dp_n, dp_p)
        return ans
