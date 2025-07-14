inf = 1 << 70


class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        dp = [1] + [inf] * (len(dungeon[0]) - 1)
        for line in reversed(dungeon):
            now = [inf]
            for i, v in enumerate(reversed(line)):
                now.append(max(min(dp[i], now[-1]) - v, 1))
            dp = now[1:]
            # print(dp)
        return dp[-1]

