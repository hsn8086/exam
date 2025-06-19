class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        dp_max = [1] + [None] * len(grid[0])
        dp_min = [1] + [None] * len(grid[0])
        for line in grid:
            now_max = [None]
            now_min = [None]
            for i, v in enumerate(line):
                lst = []
                for i in (dp_max[i], dp_min[i], now_max[-1], now_min[-1]):
                    if i is not None:
                        lst.append(i * v)
                v_max = max(lst)
                v_min = min(lst)

                now_max.append(v_max)
                now_min.append(v_min)
            dp_max = now_max[1:]
            dp_min = now_min[1:]
            # print(*dp_max, "\t", *dp_min)

        return dp_max[-1] % (10**9 + 7) if dp_max[-1] >= 0 else -1


# Solution().maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]])
