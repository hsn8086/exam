for _ in range(int(input())):
    n=int(input())
    if n%2==0:
        print(-1)
        continue
    else:
        print(n,*range(1,n))