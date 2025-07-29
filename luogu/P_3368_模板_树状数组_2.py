class DiffFenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 1)

    def _update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def update(self, index, delta):
        self._update(index, delta)
        self._update(index + 1, -delta)

    def update_range(self, start, end, delta):
        self._update(start, delta)
        self._update(end + 1, -delta)

    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res


n, m = map(int, input().split())
ft = DiffFenwickTree(n)
for i, v in enumerate(map(int, input().split()), 1):
    ft.update(i, v)

for _ in range(m):
    cmd_raw, args_raw = input().split(maxsplit=1)
    cmd = int(cmd_raw)
    args = list(map(int, args_raw.split()))

    if cmd == 1:
        x, y, k = args
        ft.update_range(x, y, k)

    else:
        x = args[0]
        print(ft.query(x))
