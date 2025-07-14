from itertools import pairwise

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    lsv = list(set(a))
    if len(lsv) == 2 and lsv[0] == -lsv[1]:
        cnt1 = a.count(lsv[0])
        cnt2 = a.count(lsv[1])
        if min(cnt1, cnt2) == n // 2 and cnt1 + cnt2 == n:
            print("Yes")
            continue

    sa = sorted(a, key=lambda x: -abs(x))
    for i, j in pairwise(pairwise(sa)):
        a1, b = i
        _, c = j
        if a1 * c != b * b:
            print("No")
            break
    else:
        print("Yes")
