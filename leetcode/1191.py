from itertools import accumulate

inf = 10**20


class Solution:
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
        dp = [-inf]
        for i in arr:
            dp.append(max(dp[-1] + i, i))
        ans1 = max(0, *dp)
        if k == 1:
            return ans1 % (10**9 + 7)
        else:
            pre = max(0, *accumulate(arr))
            suf = max(0, *accumulate(arr[::-1]))
            s = sum(arr) * (k - 2)
            return max(0, pre, suf, pre + suf, pre + suf + s, ans1) % (10**9 + 7)
