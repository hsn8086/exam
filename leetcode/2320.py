class Solution:
    def countHousePlacements(self, n: int) -> int:
        dp_t = [0]
        dp_f = [1]
        for i in range(n):
            lf, lt = dp_f[-1], dp_t[-1]
            dp_t.append(lf)
            dp_f.append(lf + lt)
        return pow(dp_f[-1] + dp_t[-1], 2, 10**9 + 7)


# print(Solution().countHousePlacements(2))
