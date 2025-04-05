for _ in range(int(input())):
    n,k=map(int, input().split())
    a=map(int, input().split())
    if sum(a)/n==k:
        print("YES")
    else:
        print("NO")
