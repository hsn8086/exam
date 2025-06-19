inf = 10**20


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        vd = {chr(i): i - 96 for i in range(97, 123)}
        for c, v in zip(chars, vals):
            vd[c] = v

        nums = [vd[c] for c in s]

        dp = [0]
        for i in nums:
            dp.append(max(dp[-1] + i, i))
        return max(dp)
