import sys
from math import ceil
from collections import defaultdict


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


input = sys.stdin.readline
for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    lst = []
    lst.extend(a)

    threshold = n - ceil((n - 1) / 2)
    copy_a = a.copy()
    qs = []
    for _ in range(q):
        i, d = map(int, input().split())
        qs.append((i, d))
        v = copy_a[i - 1]
        copy_a[i - 1] += d
        lst.append(copy_a[i - 1])

    lst.sort()

    ft = FenwickTree(len(lst) + 10)
    print()
    mp = {}
    for i, v in enumerate(lst, 1):
        mp[v] = i

    for i in a:
        ft.update(mp[i], 1)

    for i, d in qs:
        v = a[i - 1]
        ft.update(mp[v], -1)
        ft.update(mp[v + d], +1)
        a[i - 1] += d

        left, right = 0, len(lst)-1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            lose = ft.query_prefix(mp[lst[mid]])
            if lose <= threshold:
                ans = lose
                left = mid + 1
            else:
                right = mid - 1
        print(ans)
