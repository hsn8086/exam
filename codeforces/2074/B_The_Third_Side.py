for _ in range(int(input())):
    n=int(input())
    a=map(int, input().split())
    print(sum(a)-n+1)