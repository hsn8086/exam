import math


n=int(input())
lst=[]
for _ in range(n):
    x,y,z=map(int,input().split())
    lst.append((x,y,z))
lst.sort(key=lambda e:e[2])
sum_=0
for i in range(1,n):
    xa,ya,za=lst[i-1]
    xb,yb,zb=lst[i]
    sum_+=math.sqrt((xa-xb)**2+(ya-yb)**2+(za-zb)**2)

print("%.3f"%sum_)