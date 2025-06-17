import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = sorted(map(lambda inp: abs(k - int(inp)), input().split()))
    print(a[m - 1])
