import sys
from collections import defaultdict, Counter
from random import shuffle

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    mex = 0
    a_cp=a.copy()
    shuffle(a_cp)
    s = set(a_cp)
    while mex in s:
        mex += 1

    cnt = Counter(a)

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
            c_cnt = defaultdict(int)
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
