import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    max_prefix = [0]
    prefix = [0]
    for i in reversed(a):
        prefix.append(prefix[-1] + i)
    for i in a:
        max_prefix.append(max(max_prefix[-1], i))
    prefix = prefix[::-1]
    rst = []
    for i in range(n - 1, -1, -1):
        front_max = max_prefix[i]
        # print(front_max)
        e = a[i]
        rst.append(max(prefix[i], prefix[i] - e + front_max))
        # print(prefix[i])
    print(*rst)
