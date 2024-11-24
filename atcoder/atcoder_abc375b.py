import math
n=int(input())
lst=[(0,0)]
for _ in range(n):
    x,y=map(int,input().split())
    lst.append((x,y))
lst.append((0,0))
sum_=0
for i in range(1,n+2):
    last_x,last_y=lst[i-1]
    x,y=lst[i]
    sum_+=math.sqrt((last_x-x)**2+(last_y-y)**2)
print(sum_)