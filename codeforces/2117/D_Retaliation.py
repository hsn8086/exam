from itertools import pairwise

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = a[1] - a[0]

    for i, j in pairwise(a):
        if j - i != d:
            print("NO")
            break
    else:
        m = min(a)
        if m < abs(d):
            print("NO")
            continue

        if (m - abs(d)) % (n + 1) == 0:
            print("YES")
        else:
            print("NO")
