import sys
from collections import defaultdict, Counter
from random import randint


input = sys.stdin.readline


class CFDefaultDict(defaultdict):
    def __init__(self, default_factory: callable):
        super(CFDefaultDict, self).__init__()
        self.rnd = randint(57, 8086)
        self.default_factory = default_factory

    def _v(self, i):
        return i + self.rnd

    def __contains__(self, key):
        return super().__contains__(self._v(key))

    def __getitem__(self, key):
        return super().__getitem__(self._v(key))

    def __setitem__(self, key, value):
        super().__setitem__(self._v(key), value)

    def __delitem__(self, key):
        super().__delitem__(self._v(key))


class CFCounter(Counter):
    def __init__(self, iterable=None, /, **kwds):
        self.rnd = randint(57, 8086)
        super(CFCounter, self).__init__(iterable, **kwds)

    def _v(self, i):
        return i + self.rnd

    def __contains__(self, key):
        return super().__contains__(self._v(key))

    def __getitem__(self, key):
        return super().__getitem__(self._v(key))

    def __setitem__(self, key, value):
        super().__setitem__(self._v(key), value)

    def __delitem__(self, key):
        super().__delitem__(self._v(key))

    def update(self, iterable):
        for elem in iterable:
            self[elem] += 1


class CFSet:
    def __init__(self, iterable=None, /):
        self.rnd = randint(57, 8086)

        if iterable is None:
            self.s = set()
        else:
            self.s = set(map(self._v, iterable))

    def _v(self, i):
        return i + self.rnd

    def add(self, elem):
        self.s.add(self._v(elem))

    def remove(self, elem):
        self.s.remove(self._v(elem))

    def discard(self, elem):
        self.s.discard(self._v(elem))

    def __contains__(self, elem):
        return self._v(elem) in self.s

    def __iter__(self):
        for elem in self.s:
            yield elem - self.rnd

    def __len__(self):
        return len(self.s)


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    mex = 0

    s = CFSet(a)
    while mex in s:
        mex += 1

    cnt = CFCounter(a)

    left = 0
    right = mex
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        valid = True
        if mid > 0:
            for i in range(mid):
                if i not in s or cnt[i] < k:
                    valid = False
                    break
            if not valid:
                right = mid - 1
                continue

        if mid == 0:
            if k <= n:
                ans = 0
                if ans > ans:
                    ans = ans
                left = mid + 1
            else:
                right = mid - 1
        else:
            req = mid
            c_cnt = CFDefaultDict(int)
            c_seg = 0
            col = 0
            for num in a:
                if 0 <= num < req:
                    if c_cnt[num] == 0:
                        col += 1
                    c_cnt[num] += 1
                    if col == req:
                        c_seg += 1
                        c_cnt.clear()
                        col = 0
            if c_seg >= k:
                if mid > ans:
                    ans = mid
                left = mid + 1
            else:
                right = mid - 1
    print(ans)
