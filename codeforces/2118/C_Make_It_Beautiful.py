from itertools import accumulate
import bisect

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = map(int, input().split())
    init = 0
    lst = []
    for ai in a:
        # print(bin(ai))
        b = bin(ai)[2:][::-1]
        b_len = len(b)
        for i in range(64):
            if b_len <= i:
                v = "0"
            else:
                v = b[i]
            if v == "1":
                init += 1
            else:
                lst.append(2**i)
    lst.sort()
    prefix = list(accumulate(lst))

    print(bisect.bisect(prefix, k) + init)
