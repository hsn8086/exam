class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_dp = [1 << 70]
        for p in prices:
            min_dp.append(min(min_dp[-1], p))

        ans = 0
        for min_v, now_v in zip(min_dp[1:], prices):
            ans = max(ans, now_v - min_v)
        return ans
