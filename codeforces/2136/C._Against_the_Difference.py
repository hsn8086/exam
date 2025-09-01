import sys
from collections import deque

input = sys.stdin.readline
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    rec: list[deque] = [deque(maxlen=max(i, 1)) for i in range(n + 1)]
    pair = []
    for i, v in enumerate(a):
        rec[v].append(i)
        if len(rec[v]) == max(v, 1):
            pair.append((rec[v][0] + 1, i + 1, v))

    pair.sort(key=lambda t: t[1])
    dp = [0]
    if not pair:
        print(0)
        continue
    # print(pair)
    idx = 0
    start, end, v = pair[idx]
    idx += 1
    # print(pair)
    for i in range(1, n + 1):
        now = dp[-1]
        dp.append(now)
        while i == end:
            now = max(dp[start - 1] + v, now)
            if idx >= len(pair):
                break
            start, end, v = pair[idx]
            idx += 1

        dp[-1] = now
        # print(i,dp)
    print(dp[-1])
