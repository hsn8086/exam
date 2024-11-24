lst=[0]*1010
n=int(input())
for i in map(int,input().split()):
    lst[i]=1

print(sum(lst))
for i in range(len(lst)):
    if lst[i]:
        print(i,end=" ")