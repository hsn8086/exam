n,q=map(int,input().split())
d={}
for _ in range(q):
    op,data=input().split(maxsplit=1)
    if op=="1":
        i,j,k=map(int,data.split())
        d[(i,j)]=k
    else:
        i,j=map(int,data.split())
        print(d[(i,j)])