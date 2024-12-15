
from collections import Counter

import statistics
ntc=int(input())
for _ in range(ntc):
    n=int(input())
    a=[tuple(map(int,input().split())) for _ in range(n)]
    x=statistics.median_high(map(lambda e:e[0],a))
    y=statistics.median_high(map(lambda e:e[1],a))

    lst=[]
    for xp,yp in a:
        if x<=xp and y<=yp:
            lst.append(1)
        elif x>xp and y<=yp:
            lst.append(2)
        elif x<=xp and y>yp:
            lst.append(3)
        elif x>xp and y>yp:
            lst.append(4)
    ct=Counter(lst)
    if len(ct)==4:
        print(min(ct.values()))
    else:
        print(0)
    print(x,y)
    