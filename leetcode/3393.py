from functools import cache


def search(grid: list[list[int]], start_pos: tuple[int, int], start_k: int):
    @cache
    def dfs(pos: tuple[int, int], k: int):
        x, y = pos
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return 0
        if x == 0 and y == 0:
            # print(0)
            return int(grid[0][0] == k)

        return (dfs((x - 1, y), k ^ grid[x][y]) + dfs((x, y - 1), k ^ grid[x][y])) % (
            10**9 + 7
        )

    return dfs(start_pos, start_k)


class Solution:
    def countPathsWithXorValue(self, grid: list[list[int]], k: int) -> int:
        return search(grid, (len(grid) - 1, len(grid[0]) - 1), k)


# print(Solution().countPathsWithXorValue([[2, 1, 5], [7, 10, 0], [12, 6, 4]], 12))
