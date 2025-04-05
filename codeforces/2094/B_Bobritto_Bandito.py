for _ in range(int(input())):
    n,m,l,r=map(int, input().split())
    left=min(0,r-m)
    right=min(r,m)
    print(left,right)