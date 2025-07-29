for _ in range(int(input())):
    n=int(input())
    if n%2==0:
        print(-1)
        continue
    rst=[0]*n
    for i in range(1,n+1):
        rst[(i*2-1)%n]=i
    print(*rst)