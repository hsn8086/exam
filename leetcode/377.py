class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp=[1]+[0]*(target+max(nums))
        for i in range(target):
            for step in nums:
                dp[i+step]+=dp[i]
        return dp[target]