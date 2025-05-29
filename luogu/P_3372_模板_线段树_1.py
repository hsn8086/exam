import sys

input = sys.stdin.readline


class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query_prefix(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

    def query(self, index):
        return self.query_range(index, index)

    def query_range(self, left, right):
        return self.query_prefix(right) - self.query_prefix(left - 1)


class RURQFenwickTree:
    def __init__(self, size):
        self.ft1 = FenwickTree(size)
        self.ft2 = FenwickTree(size)

    def _update(self, index, delta):
        self.ft1.update(index, delta)
        self.ft2.update(index, delta * index)

    def update(self, index, delta):
        self.update_range(index, index, delta)

    def update_range(self, left, right, delta):
        self._update(left, delta)
        self._update(right + 1, -delta)

    def query_prefix(self, index):
        return (index + 1) * self.ft1.query_prefix(index) - self.ft2.query_prefix(index)

    def query_range(self, left, right):
        return self.query_prefix(right) - self.query_prefix(left - 1)

    def query(self, index):
        return self.query_range(index, index)


n, m = map(int, input().split())
a = list(map(int, input().split()))

rurq_ft = RURQFenwickTree(n)
for i, v in enumerate(a, 1):
    rurq_ft.update(i, v)


for i in range(m):
    pin = map(int, input().split())
    cmd = next(pin)
    if cmd == 1:
        x, y, k = pin
        rurq_ft.update_range(x, y, k)
    elif cmd == 2:
        x, y = pin
        print(rurq_ft.query_range(x, y))
