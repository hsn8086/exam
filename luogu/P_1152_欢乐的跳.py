scaner=map(int,input().split())
n=next(scaner)
a=list(scaner)
lst=[1]*(n-1)
for i in range(1,len(a)):
    d=abs(a[i-1]-a[i])
    if 0<d<n:
        lst[d-1]=0

if sum(lst)==0:
    print("Jolly")
else:
    print("Not jolly")