from itertools import combinations
a=list(map(int,input().split()))
b=list(map(int,input().split()))
count=0
for al,bl in combinations(zip(a,b),2):
    ali,alc=al
    bli,blc=bl
    if (ali>bli and alc<blc) or (ali<bli and alc>blc):
        count+=1
print(count)