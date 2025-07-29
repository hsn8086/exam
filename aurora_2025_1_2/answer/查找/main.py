import bisect

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(bisect.bisect_left(a, k) + 1)
