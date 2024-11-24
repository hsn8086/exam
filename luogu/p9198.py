n,m,q=map(int,input().split())
# eq_sq=[[] for i in m]
changed_map={}
neq_set=set()
for _ in range(q):
    i,j,t,c=map(int,input().split())
    changed_map[(i,j,t)]=(changed_map.get((i,j,t),0)+c)%256

    if changed_map.get((i,m-j+1,t),0)!=changed_map.get((i,j,t),0):
        print("No")
        neq_set.add((i,j,t))
        continue

    if (i,j,t) in neq_set:
        neq_set.remove((i,j,t))
    
    if (i,m-j+1,t) in neq_set:
        neq_set.remove((i,m-j+1,t))

    if len(neq_set)==0:
        print("Yes")
    else:
        print("No")