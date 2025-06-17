inf = 10**20


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dis = [0, 0] + [inf] * (len(cost))
        for i, c in enumerate(cost):
            dis[i + 1] = min(dis[i + 1], dis[i] + c)
            dis[i + 2] = min(dis[i + 2], dis[i] + c)
        return dis[-2]
