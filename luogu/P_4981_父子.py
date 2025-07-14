import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    print(pow(n, n - 1, 10**9 + 9))
