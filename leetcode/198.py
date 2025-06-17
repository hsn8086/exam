class Solution:
    def rob(self, nums: list[int]) -> int:
        l2 = 0
        l1 = 0
        for i in nums:
            l2, l1 = l1, max(l1, l2 + i)

        return l1
