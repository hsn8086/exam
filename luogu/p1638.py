n,m=map(int,input().split())
a=list(map(int,input().split()))
exists={}

min_=float("+inf")
min_lr=(0,0)
left=0
right=-1
while 1:
    right+=1
    if right >= n:
        break
    exists[a[right]]=exists.get(a[right],0)+1
    if len(exists)==m:
        while 1:
            if exists[a[left]]>=2:
                exists[a[left]]-=1
                left+=1
                
            else:
                break
        if right-left+1<min_:
            min_=right-left+1
            min_lr=(left+1,right+1)
print(*min_lr)