# B. Battle for Survive B. 生存之战
# time limit per test
# 1 second
# 每个测试的时间限制
# 1 秒
# memory limit per test
# 256 megabytes
# 每个测试的内存限制
# 256 兆字节

# Eralim, being the mafia boss, manages a group of n
# fighters. Fighter i has a rating of ai.
# 作为黑帮老大的 Eralim 管理着一群 n 战士。战士 i 的评级为 ai

# 。

# Eralim arranges a tournament of n−1
# battles, in each of which two not yet eliminated fighters i and j (1≤i<j≤n) are chosen, and as a result of the battle, fighter i is eliminated from the tournament, and the rating of fighter j is reduced by the rating of fighter i. That is, aj is decreased by ai. Note that fighter j's rating can become negative. The fighters indexes do not change.
# Eralim 安排了一场 n−1 战斗的锦标赛，每场比赛中选择两名尚未被淘汰的战士 i 和 j （ 1≤i<j≤n ），战斗结果是战士 i 被淘汰出锦标赛，战士 j 的评分减少战士 i 的评分。也就是说， aj 减少了 ai 。请注意，战士 j

# 的评分可能会变为负数。战士的索引不会改变。

# Eralim wants to know what maximum rating the last remaining fighter can preserve if he chooses the battles optimally.
# Eralim 想知道如果他选择战斗最优，最后剩下的战士能保留的最大评分是多少。
# Input 输入

# Each test contains multiple test cases. The first line contains the number of test cases t
# (1≤t≤104). The description of the test cases follows.
# 每个测试包含多个测试用例。第一行包含测试用例的数量 t （ 1≤t≤104

# ）。接下来是测试用例的描述。

# The first line of each test case contains a single integer n
# (2≤n≤2⋅105) — the number of fighters.
# 每个测试用例的第一行包含一个整数 n ( 2≤n≤2⋅105

# ) —— 战士的数量。

# The second line of each test case contains n
# integers a1,a2,…an (1≤ai≤109) — the ratings of the fighters.
# 每个测试用例的第二行包含 n 个整数 a1,a2,…an ( 1≤ai≤109

# ) —— 战士的评分。

# The sum of n
# over all testcases does not exceed 2⋅105.
# 所有测试用例中 n 的总和不超过 2⋅105

# 。
# Output 输出

# For each testcase, output a single integer — the maximum rating that the last remaining fighter can preserve.
# 对于每个测试用例，输出一个整数——最后一个留下的战士可以保留的最大评分。
# Example 示例
# Input 输入
# Copy 复制

# 5
# 2
# 2 1
# 3
# 2 2 8
# 4
# 1 2 4 3
# 5
# 1 2 3 4 5
# 5
# 3 2 4 5 4

# Output 输出
# Copy 复制

# -1
# 8
# 2
# 7
# 8

# Note 笔记

# In the first example, you can arrange a fight between fighters with indices 1
# and 2, where the fighter with index 2 will win. The rating of the last fighter, that is, the fighter with index 2, will be 1−2=−1.
# 在第一个示例中，您可以安排索引为 1 和 2 的战士之间的战斗，其中索引为 2 的战士将获胜。最后一名战士的评分，即索引为 2 的战士，将是 1−2=−1

# 。

# In the second example, you can first conduct a fight between fighters with indices 1
# and 2, where the fighter with index 2 will win, and then conduct a fight between fighters with indices 2 and 3, where the fighter with index 3 will win.
# 在第二个示例中，您可以首先进行索引为 1 和 2 的战士之间的战斗，其中索引为 2 的战士将获胜，然后进行索引为 2 和 3 的战士之间的战斗，其中索引为 3

# 的战士将获胜。

# The rating of the fighter with index 2
# after the first fight will be 2−2=0. The rating of the fighter with index 3 after the second fight will be 8−0=8.
# 编号为 的选手 2 在第一场比赛后的评分将是 2−2=0 。编号为 的选手 3 在第二场比赛后的评分将是 8−0=8 。

from typing import Iterable
def solve(n: int, an: Iterable[int]) -> int:
    sum=0
    for i in range(n-2):
        sum+=next(an)
    return sum-next(an)+next(an)


count_of_tc = int(input())
for i in range(count_of_tc):
    n = int(input())
    an = map(int, input().split())
    print(solve(n, an))
