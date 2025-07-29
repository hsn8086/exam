from collections import defaultdict


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


def clac(a, prefix, st: SparseTable, l, r):
    max_ = st.query(l - 1, r - 1)

    red = prefix[min(r, len(prefix) - 1)] - prefix[max(l - 2, 0)]

    if r < len(a):
        red -= abs(a[r] - max_)

    if l - 2 >= 0:
        red -= abs(a[l - 2] - max_)
    return red


for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    prefix = [0]
    init = 0
    for i in range(n - 1):
        init += abs(a[i] - a[i + 1])
        prefix.append(init)
    diff = init - x
    if diff <= 0:
        print(0)
        continue
    st = SparseTable(a, max)
    # print(clac(a, prefix, st, 2, 4))
    min_d = float("+inf")
    for i in range(n - 1):
        # bin search
        l = i + 1
        r = n

        while l < r:
            mid = (l + r) // 2
            # print(clac(a, prefix, st, i + 1, mid), diff, i + 1, mid)
            if clac(a, prefix, st, i + 1, mid) < diff:
                l = mid + 1
            else:
                r = mid
                min_d = min(min_d, r - i)
        if clac(a, prefix, st, i + 1, n) >=diff:
            min_d = min(min_d, n-i)
    print(min_d)
