from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        cte = list(Counter(nums).items())
        cte.sort()
        data = []
        tmp = []
        for i in cte + [(-1, 0)]:
            if tmp and tmp[-1][0] != i[0] - 1:
                data.append(tmp)
                tmp = []
            tmp.append(i)

        ans = 0
        for d in data:
            dp = [0, 0]
            for n, v in d:
                dp.append(max(dp[-2] + n * v, dp[-1]))
            ans += dp[-1]
        return ans
    

