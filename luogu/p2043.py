import math
from collections import OrderedDict

lst = [False, False] + [True for i in range(10000 - 1)]
for i in range(2, math.ceil(math.sqrt(10001))):
    for j in range(i, 10001):
        if i * j > 9999:
            break
        lst[i * j] = False

inp = int(input())
rtd = {}
for i in range(1, inp + 1):
    # if lst[i]:
    #     rtd[i] = rtd.get(i, 0) + 1
    #     continue
    while i != 1:
        for j, v in enumerate(lst):
            if v:
                if i % j == 0:
                    i //= j
                    rtd[j] = rtd.get(j, 0) + 1
for p,a in sorted(rtd.items(),key= lambda x:x[0]):
    print(p,a)