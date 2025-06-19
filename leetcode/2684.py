class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        dp = [(0, True) for _ in range(len(grid) + 2)]
        max_x = 0
        for x, col in enumerate(zip(*grid)):
            now = []
            for y, v in enumerate(col):
                if (
                    (dp[y][1] and dp[y][0] < v)
                    or (dp[y + 1][1] and dp[y + 1][0] < v)
                    or (dp[y + 2][1] and dp[y + 2][0] < v)
                ):
                    now.append((v, True))
                    max_x = x
                else:
                    now.append((v, False))
            dp = [(0, False)] + now + [(0, False)]
        return max_x


# print(Solution().maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]))
