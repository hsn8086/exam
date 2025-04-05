import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    min_ = float("inf")
    for i in range(n):
        for j in range(i, min(i + 32, n)):
            if (a[i] ^ a[j]) >= k:
                min_ = min(min_, j - i + 1)
                break

    print(min_ if min_ != float("inf") else -1)



