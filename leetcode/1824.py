inf = 1 << 70


class Solution:
    def minSideJumps(self, obstacles: list[int]) -> int:
        dp = [1, 0, 1]
        for i in obstacles:
            now = dp
            if i != 0:
                now[i - 1] = inf
            now = [
                min(now[0], now[1] + 1, now[2] + 1),
                min(now[0] + 1, now[1], now[2] + 1),
                min(now[0] + 1, now[1] + 1, now[2]),
            ]
            if i != 0:
                now[i - 1] = inf
            
            # print(now)
            dp = now
        return min(dp)

# Solution().minSideJumps([0,1,2,3,0])