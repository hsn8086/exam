# MOD = 998244353


# def main():
#     import sys

#     input = sys.stdin.readline  # 使用更标准的输入方式，而不是 sys.stdin.read()

#     # 预计算阶乘到 1e6
#     maxn = 10**6
#     fact = [1] * (maxn + 1)
#     for i in range(1, maxn + 1):
#         fact[i] = fact[i - 1] * i % MOD

#     T = int(input())
#     for _ in range(T):
#         # 读取一行并分割成数字，过滤掉 0
#         a = list(map(int, input().strip().split()))
#         a = [x for x in a if x != 0]

#         sum_total = sum(a)
#         # if sum_total % 2 != 0:
#         #     print(0)
#         #     continue
#         target = sum_total // 2

#         # 计算 product_all = product(inv(fact[x]) for x in a)
#         # 直接使用费马小定理计算逆元
#         product_all = 1
#         for x in a:
#             inv_fact_x = pow(fact[x], MOD - 2, MOD)
#             product_all = product_all * inv_fact_x % MOD

#         # 使用动态规划计算子集和
#         dp = [0] * (target + 1)
#         dp[0] = 1
#         for x in a:
#             for j in range(target, x - 1, -1):
#                 dp[j] = (dp[j] + dp[j - x]) % MOD

#         count_subsets = dp[target]
#         if count_subsets == 0:
#             print(0)
#             continue

#         fact_target = fact[target]
#         part1 = count_subsets * fact_target % MOD
#         part2 = fact_target * product_all % MOD
#         total = part1 * part2 % MOD
#         if sum_total % 2 == 0:
#             print(total)
#         else:
#             print(total * 2 % MOD)


# if __name__ == "__main__":
#     main()
# from random import shuffle
# from collections import Counter
# import math

# MOD = 998244353


# def count(counts):
#     total = sum(counts)

#     denominator = 1
#     for cnt in counts:
#         denominator *= math.factorial(cnt)

#     return math.factorial(total) // denominator


# def find_partitions(a, target):
#     n = len(a)

#     dp = [[0] * (target + 1) for _ in range(n + 1)]
#     dp[0][0] = 1

#     for i in range(1, n + 1):
#         for j in range(target + 1):
#             dp[i][j] = dp[i - 1][j]
#             if j >= a[i - 1]:
#                 dp[i][j] += dp[i - 1][j - a[i - 1]]

#     if dp[n][target] == 0:
#         return []


#     def backtrack(i, current_sum, path_indices):
#         if current_sum == 0:
#             b = [a[idx] for idx in path_indices]
#             c = [a[idx] for idx in range(n) if idx not in set(path_indices)]
#             yield (b, c)
#             return
#         if i == 0 or current_sum < 0:
#             return
#         if current_sum >= a[i - 1] and dp[i - 1][current_sum - a[i - 1]] > 0:
#             yield from backtrack(i - 1, current_sum - a[i - 1], path_indices + [i - 1])
#         if dp[i - 1][current_sum] > 0:
#             yield from backtrack(i - 1, current_sum, path_indices)

#     yield from backtrack(n, target, [])


# for _ in range(int(input())):
#     a = list(filter(lambda x: x, map(int, input().split())))
#     value = sum(a)
#     partitions = find_partitions(a, value // 2)
#     cnt = 0
#     for b, c in partitions:
#         cnt += count(b) * count(c) % MOD
#     print(cnt % MOD)


# for _ in range(int(input())):
#     a = list(map(int, input().split()))
#     value = sum(a)

#     # Initialize DP: each element will be a tuple (max_value, list_of_solutions)
#     dp = [(0, []) for _ in range(value + 1)]

#     for num in a:
#         for j in range(value, num - 1, -1):
#             if dp[j - num][0] + num > dp[j][0]:
#                 dp[j] = (dp[j - num][0] + num, [s + [num] for s in dp[j - num][1]])
#             elif dp[j - num][0] + num == dp[j][0]:
#                 dp[j][1].extend([s + [num] for s in dp[j - num][1]])

#     # Filter solutions that exactly match the target value
#     target = value
#     exact_solutions = [s for s in dp[target][1] if sum(s) == target]

#     print(f"Maximum value: {dp[target][0]}")
#     print(f"Number of solutions: {len(exact_solutions)}")
#     print("Solutions:")
#     for sol in exact_solutions:
#         print(sol)

# def dfs(a: list, sel: list, start: int, now_value: int, target: int):
#     if now_value == target:
#         tag = [False] * 26
#         for i in sel:
#             tag[i] = True
#         return count([a[i] for i in range(len(tag)) if tag[i]]) * count(
#             [a[i] for i in range(len(tag)) if not tag[i]]
#         )
#     elif now_value > target:
#         return 0
#     if start == len(a):
#         return 0
#     return dfs(a, sel + [start], start + 1, now_value + a[start], target) + dfs(
#         a, sel, start + 1, now_value, target
#     )


# for _ in range(int(input())):
#     a = list(map(int, input().split()))
#     total = sum(a)
#     target = total // 2

#     print(dfs(a, [], 0, 0, target))
from random import shuffle
from collections import Counter
import math


MOD = 998244353


def count(counts):
    total = sum(counts)

    denominator = 1
    for cnt in counts:
        denominator *= math.factorial(cnt)

    return math.factorial(total) // denominator % MOD


for _ in range(int(input())):
    a = list(filter(lambda x: x, map(int, input().split())))
    total = sum(a)
    target = total // 2
    n = len(a)

    dp = [None] * (target + 1)
    dp[0] = []

    for num in a:
        for j in range(target, num - 1, -1):
            if dp[j - num] is not None and dp[j] is None:
                dp[j] = dp[j - num] + [num]
    dp2 = [0] * (target + 1)
    dp2[0] = 1
    for x in a:
        for j in range(target, x - 1, -1):
            dp2[j] = (dp2[j] + dp2[j - x]) % MOD
    # print(dp)
    selected = []
    for j in range(target, -1, -1):
        if dp[j] is not None:
            selected = dp[j]
            break
    shuffle(selected)
    selected_cnt = Counter(selected)

    for i, v in enumerate(a):
        if selected_cnt.get(v, 0):
            selected_cnt[v] -= 1
            a[i] = 0
    a = list(filter(lambda x: x, a))
    # print(dp2[target])
    print(count(selected) * count(a) * dp2[target] % MOD)
