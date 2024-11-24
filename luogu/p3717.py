n,m,r=map(int,input().split())
lst=[]
for _ in range(m):
    x,y=map(int,input().split())
    lst.append((x,y))
count=0
for x in range(1,n+1):
    for y in range(1,n+1):
        for xm,ym in lst:
            if (x-xm)**2+(y-ym)**2<=r**2:
                count+=1
                break
print(count)