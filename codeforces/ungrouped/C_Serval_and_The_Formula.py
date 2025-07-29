for _ in range(int(input())):
    a, b = map(int, input().split())
    m = max(a, b)
    if a == b:
        print(-1)
        continue
    k=2**31 - m

    #print((a+k)^(b+k)==(a+k+b+k))
    print(2**30 - m)
