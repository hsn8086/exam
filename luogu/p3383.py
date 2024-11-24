import math

lst = [False, False] + [True for i in range(10**8)]
for i in range(2, math.ceil(math.sqrt(10**8))):
    if not lst[i]:
        continue
    for j in range(i, 10**8):

        if i * j > 10**8:
            break
        lst[i * j] = False

lst = list(map(lambda x: x[0], filter(lambda x: x[1], enumerate(lst))))
ntc = int(input())
for _ in range(ntc):
    inp=int(input())
    print(lst[inp-1])