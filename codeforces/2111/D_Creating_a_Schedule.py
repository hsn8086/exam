for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))

    for i in range(n//2):
        print(a[i],a[-i-1],a[i],a[-i-1],a[i],a[-i-1],)
    
    for i in range(n-n//2):
        print(a[-i-1],a[i],a[-i-1],a[i],a[-i-1],a[i],)
