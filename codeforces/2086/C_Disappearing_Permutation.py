def search(id_:int,a:list,cnt:list,tag:list,start:int):
    stop=start
    tag[start]=id_
    start=a[start]
    cnt_=1
    while stop!=start:
        tag[start]=id_
        start=a[start]
        cnt_+=1
    cnt[id_]+=cnt_
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=input()
    a=[0]+list(map(int, input().split()))
    cnt=[0]*(10**5+10)
    tag=[0]*(10**5+10)
    d=map(int, input().split())

    id_=0
    for i,v in enumerate(a):
        if not tag[i]:
            id_+=1
            search(id_,a,cnt,tag,i)

    cnt_=0
    for i in d:
        if cnt[tag[i]]:
            cnt_+=cnt[tag[i]]
            cnt[tag[i]]=0
        print(cnt_,end=" ")
    print()