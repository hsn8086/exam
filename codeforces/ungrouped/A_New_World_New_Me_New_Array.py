from math import ceil
for _ in range(int(input())):
    n,k,p=map(int, input().split())
    rst=ceil(abs(k)/p)
    if rst>n:
        print(-1)
    else:
        print(rst)