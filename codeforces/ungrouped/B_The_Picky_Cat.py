for _ in range(int(input())):
    n=int(input())
    a=list(map(lambda x: abs(int(x)), input().split()))
    op=a[0]
    a.sort()
    if op<=a[n//2]:
        print("YES")
    else:
        print("NO")