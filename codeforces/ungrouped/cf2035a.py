num_of_tc=int(input())
for _ in range(num_of_tc):
    n,m,r,c=map(int,input().split())
    type_a=(n-r)*(m-1)+(m-c)
    type_b=n-r
    print(type_a+type_b*m)