import sys
from math import gcd


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
        j = self.log[right - left + 1]
        return self.func(self.st[j][left], self.st[j][right - (1 << j) + 1])


input = sys.stdin.readline
n, m = map(int, input().split())
st = SparseTable(list(map(int, input().split())), func=gcd)

for _ in range(m):
    l, r = map(int, input().split())
    print(st.query(l - 1, r - 1))
