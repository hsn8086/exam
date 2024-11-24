from math import isqrt
from collections import Counter

ntc = int(input())
for _ in range(ntc):
    k = int(input())
    a = list(map(int, input().split()))
    count = Counter(a)
    area = k - 2

    for i in range(1, isqrt(area) + 1):
        if area % i == 0:
            j = area // i
            if i in count and j in count:
                if i == j:
                    if count[i] >= 2:
                        print(i, j)
                        break
                else:
                    print(i, j)
                    break
    else:
        print(-1, -1)


