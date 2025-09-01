from collections import deque
from itertools import accumulate

for _ in range(int(input())):
    n, m, k, d = map(int, input().split())
    lst = []
    for _ in range(n):
        mono_que = deque()
        mono_que.append((-1, 0))
        for i, deep in enumerate(map(int, input().split())):
            # print(dp[-d-1:],deep)
            while mono_que:
                i_ = mono_que[0][0]
                if i - i_ > d + 1:
                    mono_que.popleft()
                else:
                    break
            # print(deep,mono_que)
            min_ = mono_que[0][1]
            v = deep + 1 + min_
            # print(mono_que[-1])
            while mono_que and mono_que[-1][1] > v:
                mono_que.pop()
            # print(i,v,deep)
            print(v)
            mono_que.append((i, v))
        print()
        # print(dp)
        lst.append(mono_que[0][1] + 1)

    prefix = list(accumulate(lst, initial=0))
    min_ = 1 << 70
    for i in range(len(prefix) - k):
        min_ = min(min_, prefix[i + k] - prefix[i])

    # print(min_)
