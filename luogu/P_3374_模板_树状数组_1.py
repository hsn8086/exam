class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)

n, m = map(int, input().split())
ft = FenwickTree(n)
for i, v in enumerate(map(int, input().split()), 1):
    ft.update(i, v)

for _ in range(m):
    cmd, x, y = map(int, input().split())
    if cmd == 1:
        ft.update(x, y)
    else:
        print(ft.range_query(x, y))
