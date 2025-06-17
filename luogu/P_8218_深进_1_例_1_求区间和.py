from itertools import accumulate

n = int(input())
prefix = [0] + list(accumulate(map(int, input().split())))

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(prefix[r] - prefix[l - 1])
