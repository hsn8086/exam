from itertools import accumulate

inf = 10**20


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        dp = [-inf]
        for i in nums:
            dp.append(max(dp[-1] + i, i))
        prefix = list(accumulate(nums))
        suffix = list(accumulate(nums[::-1]))[::-1]

        max_pre = 0
        ans = -inf
        for pre, suf in zip(prefix, suffix):
            ans = max(ans, max_pre + suf)
            max_pre = max(max_pre, pre)
        return max(ans, *dp)
