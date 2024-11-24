# def solve(n, a):
#     asum = [0]
#     for i in range(n):
#         asum.append(a[i] + asum[-1])
#     end_point = 0
#     count = 0
#     for i in range(n + 1):
#         for j in range(end_point, i):
#             if asum[i] - asum[j] == 0:
#                 end_point = i
#                 count += 1
#                 break
#     return count


# num_of_tc = int(input())
# for _ in range(num_of_tc):
#     n = int(input())
#     a = list(map(int, input().split()))
#     print(solve(n, a))
def solve(n, a):
    prefix = [0]
    for num in a:
        prefix.append(prefix[-1] + num)

    dp = [0] * (n + 1)
    seen = {0: 0}

    for i in range(1, n + 1):
        if prefix[i] in seen:
            last = seen[prefix[i]]
            dp[i] = max(dp[i - 1], dp[last] + 1)
        else:
            dp[i] = dp[i - 1]

        seen[prefix[i]] = i
    return dp[n]


t = int(input())

for _ in range(t):
    n = int(input())
    a = map(int, input().split())
    print(solve(n, a))


