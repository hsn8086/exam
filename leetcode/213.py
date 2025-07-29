class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1 = [0, 0]
        dp2 = [0, 0]
        for i, v in enumerate(nums, 1):
            if i == len(nums):
                dp1.append(max(dp1[-1], dp1[-2]))
            else:
                dp1.append(max(dp1[-1], dp1[-2] + v))
        for v in nums[1:]:
            dp2.append(max(dp2[-1], dp2[-2] + v))

        return max(dp1[-1], dp2[-1])
