from typing import Callable


class SparseTable:
    def __init__(self, arr: list, func: Callable = min):
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

    def query(self, left: int, right: int):
        j = self.log[right - left + 1]
        return self.func(self.st[j][left], self.st[j][right - (1 << j) + 1])


n, q = map(int, input().split())
a = [int(input()) for _ in range(n)]
st_max = SparseTable(a, max)
st_min = SparseTable(a, min)


for _ in range(q):
    left, right = map(int, input().split())
    print(st_max.query(left - 1, right - 1) - st_min.query(left - 1, right - 1))
