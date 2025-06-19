class SparseTable:
    def __init__(self, arr, func=min):
        self.func = func
        self.n = len(arr)
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1
        self.k = self.log[self.n]
        self.st = [[0] * (self.n) for _ in range(self.k + 1)]
        self.st[0] = arr
        for j in range(1, self.k + 1):
            i = 0
            while i + (1 << j) <= self.n:
                self.st[j][i] = self.func(
                    self.st[j - 1][i], self.st[j - 1][i + (1 << (j - 1))]
                )
                i += 1

    def query(self, left, right):
        print(left, right)
        j = self.log[right - left + 1]
        return self.func(self.st[j][left], self.st[j][right - (1 << j) + 1])


class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        if len(grid[0]) == 1:
            return grid[0][0]
        dp = SparseTable([0] * (len(grid[0])))
        for line in grid:
            now = []
            for i, v in enumerate(line):
                if i == 0:
                    now.append(dp.query(1, len(grid[0]) - 1) + v)
                elif i == len(grid[0]) - 1:
                    now.append(dp.query(0, len(grid[0]) - 2) + v)
                else:
                    now.append(
                        min(dp.query(0, i - 1), dp.query(i + 1, len(grid[0]) - 1)) + v
                    )
            dp = SparseTable(now)
        return dp.query(0, len(grid[0]) - 1)


Solution().minFallingPathSum([[7]])
