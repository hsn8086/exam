from math import ceil

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    lst = [1]
    for i, v in enumerate(a[1:], 1):
        if a[i - 1] + 1 < v:
            lst.append(1)
        elif a[i - 1] == v:
            ...
        else:
            lst[-1] += 1
    # print(lst)
    print(sum(ceil(i / 2) for i in lst))
