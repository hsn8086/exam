# import sys
# n = int(sys.stdin.buffer.readline())
# s = sorted(map(hash, sys.stdin.buffer.readlines()))
# print(n - sum((s[i] == s[i - 1]) for i in range(n - 1, 0, -1)))

print(len(set(input() for _ in range(int(input())))))
