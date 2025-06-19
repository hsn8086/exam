inf = 10**20


class Solution:
    def maximumsSplicedArray(self, nums1: list[int], nums2: list[int]) -> int:
        nums = [a - b for a, b in zip(nums1, nums2)]

        ans = 0
        dp = -inf
        for i in nums:
            dp = max(dp + i, i)
            ans = max(ans, dp)

        ans2 = 0
        dp = inf
        for i in nums:
            dp = min(dp + i, i)
            ans2 = max(ans2, -dp)
        return max(sum(nums2) + ans, sum(nums1) + ans2)
