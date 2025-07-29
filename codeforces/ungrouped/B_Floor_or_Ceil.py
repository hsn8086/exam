from math import ceil,log2
def sol_max(x,n,m):
    if m>log2(x)+3:
        return 0
    while n or m:
        if x==0:
            break
        if x%2 and n:
            x=x//2+1
            n-=1
        elif m:
            x=x//2
            m-=1
        else:
            x=ceil(x/2)
            n-=1
        
    return x
def sol_min(x,n,m):
    if m>log2(x)+3:
        return 0
    while n or m:
        if x==0:
            break
        if x%2 and m:
            x=x//2
            m-=1
        elif n:
            x=ceil(x/2)
            n-=1
        else:
            x=x//2
            m-=1
        
    return x
for _ in range(int(input())):
    x,n,m=map(int, input().split())
    print(sol_min(x,m,n),sol_max(x,m,n))