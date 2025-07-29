import bisect

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = map(int, input().split())
    for i,v in enumerate(a):
        if v<k:
            print(i)
