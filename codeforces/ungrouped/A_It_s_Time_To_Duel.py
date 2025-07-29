from itertools import pairwise


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for b, c in pairwise(a):
        if b == c == 0:
            print("YES")
            break
    else:
        if a.count(1) == n:
            print("YES")
        else:
            print("NO")
