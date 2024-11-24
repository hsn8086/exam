
op_lst=[]
n,m=map(int,input().split())
for _ in range(n):
    op_lst.append(tuple(map(int,input().split())))
for _ in range(m):
    lst=[i for i in range(0,10)]
    left,right=map(int,input().split())
    for op in op_lst[left+1:right+2]:
        il,ir=op
        lst[il],lst[ir]=lst[ir],lst[il]
    print(*lst)