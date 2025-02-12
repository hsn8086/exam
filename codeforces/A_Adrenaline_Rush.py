n=int(input())
a=list(map(int,input().split()))
count=0
rst=[]
for i in range(n,0,-1):
    for j in range(i-1,0,-1):
        rst.append((i,j))
        count+=1
lst=list(range(n,0,-1))
for i in a:
    l_=[]
    for idx,j in enumerate(lst):
        if i==j:
            break
        l_.append(j)
    lst.pop(idx)
    for j in l_[::-1]:
        rst.append((i,j))
        count+=1
print(count)
[print(*t) for t in rst]
    