for _ in range(int(input())):
    n,m,k=map(int, input().split())
    cy=max(k,n//(m+1))
    print(*(i%cy for i in range(n)))