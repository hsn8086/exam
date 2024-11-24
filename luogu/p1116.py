n=int(input())
a=[]
while len(a)<n:
    inp=list(map(int,input().split()))

    a.extend(inp)
    
count=0
new_count=1
while new_count!=0:
    new_count=0
    for i in range(1,n):
        if a[i]<a[i-1]:
            a[i],a[i-1]=a[i-1],a[i]
            new_count+=1
    count+=new_count

print(count)