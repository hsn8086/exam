inf = 1 << 70


class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        dp = [0] + [-inf] * (len(coins[0]) - 1)
        dp2 = [0] + [-inf] * (len(coins[0]) - 1)
        dp3 = [0] + [-inf] * (len(coins[0]) - 1)
        for line in coins:
            now = [-inf]
            now2 = [-inf]
            now3 = [-inf]
            for i, v in enumerate(line):
                now3.append(max(now2[-1], dp2[i], now3[-1] + v, dp3[i] + v))
                now2.append(max(now[-1], dp[i], now2[-1] + v, dp2[i] + v))
                now.append(max(now[-1], dp[i]) + v)

            dp = now[1:]
            dp2 = now2[1:]
            dp3 = now3[1:]
        return dp3[-1]
