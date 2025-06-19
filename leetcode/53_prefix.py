from itertools import accumulate

inf = 10**20


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        prefix = list(accumulate(nums))

        dp_min = 0
        ans = -inf
        for i in prefix:
            ans = max(i - dp_min, ans)
            dp_min = min(dp_min, i)

        return ans

