from collections import Counter


class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        cte = list(Counter(power).items())
        cte.sort()
        data = []
        tmp = []
        for i in cte + [(-1, 0)]:
            if tmp and tmp[-1][0] != i[0] - 1 and tmp[-1][0] != i[0] - 2:
                data.append(tmp)
                tmp = []
            tmp.append(i)

        ans = 0
        for d in data:
            dp = [0, 0, 0]
            for i, da in enumerate(d):
                n, v = da
                dp.append(dp[-3] + n * v)
                if i >= 2 and n - d[i - 2][0] > 2:
                    dp[-1] = max(dp[-1], dp[-3] + n * v)
                else:
                    dp[-1] = max(dp[-1], dp[-3])
                if i >= 2 and n - d[i - 1][0] > 2:
                    dp[-1] = max(dp[-1], dp[-2] + n * v)
                else:
                    dp[-1] = max(dp[-1], dp[-2])

            ans += dp[-1]
        return ans


print(Solution().maximumTotalDamage([1, 1, 3, 4]))
