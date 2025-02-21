import sys
import random
from bisect import bisect_left, insort
import heapq


class bset:
    def __init__(self, iter_):
        lst = list(iter_)
        heapq.heapify(lst)
        sorted_lst = [heapq.heappop(lst)]
        while lst:
            e = heapq.heappop(lst)
            if sorted_lst[-1] != e:
                sorted_lst.append(e)
        self.lst = sorted_lst

    def add(self, item):
        if item in self:
            return
        else:
            insort(self.lst, item)

    def __contains__(self, item):
        i = bisect_left(self.lst, item)
        if i != len(self.lst) and self.lst[i] == item:
            return True
        return False


# 优化因子分解：只预计算到所需的最大值
MAX_N = 200001
fac = [[] for _ in range(MAX_N)]
for i in range(1, int(MAX_N**0.5) + 1):
    for j in range(i, MAX_N, i):
        fac[j].append(i)
        if i != j // i:  # 避免平方数重复
            fac[j].append(j // i)

input = sys.stdin.readline
n, m, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
random.shuffle(a)
random.shuffle(b)
sum_a = sum(a)
sum_b = sum(b)
a_ = bset(map(lambda ai: (sum_a - ai), a))
b_ = bset(map(lambda bi: (sum_b - bi), b))


for _ in range(q):
    k = int(input())
    ft = fac[abs(k)]
    for i in ft:
        if (i in a_ and k // i in b_) or (-i in a_ and -(k // i) in b_):
            print("YES")
            break
    else:
        print("NO")
