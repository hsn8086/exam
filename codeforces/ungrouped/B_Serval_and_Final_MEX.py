for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    first_zero=None
    for i,v in enumerate(a):
        if v==0:
            first_zero=i
            break
    rst=[]
    if i==0:
        rst.append((1,2))

        a[0:2]=[1]
        first_zero=None
        for i,v in enumerate(a):
            if v==0:
                first_zero=i
                break
    
    if first_zero:
        rst.append((2,len(a)))
        rst.append((1,2))
    else:
        rst.append((1,len(a)))
    print(len(rst))
    for i in rst:
        print(*i)
    
