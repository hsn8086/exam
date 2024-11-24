n=int(input())
x_lst=list(map(int,input().split()))
y_lst=list(map(int,input().split()))
r_lst=list(map(int,input().split()))
x1,y1,x2,y2=map(int,input().split())
count=0
for x,y,r in zip(x_lst,y_lst,r_lst):
    dx1=x1-x
    dx2=x2-x
    dy1=y1-y
    dy2=y2-y
    if dx1**2+dy1**2<=r**2 and dx2**2+dy2**2>r**2:
        count+=1
    if dx1**2+dy1**2>r**2 and dx2**2+dy2**2<=r**2:
        count+=1
print(count)