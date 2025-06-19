from itertools import accumulate

inf = 10**20


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        vd = {chr(i): i - 96 for i in range(97, 123)}
        for c, v in zip(chars, vals):
            vd[c] = v

        nums = [vd[c] for c in s]

        prefix = accumulate(nums)

        dp_min = 0
        ans = 0
        for i in prefix:
            ans = max(i - dp_min, ans)
            dp_min = min(dp_min, i)

        return ans
