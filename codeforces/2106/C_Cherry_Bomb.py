
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    xc = None
    posb = True
    for i in range(n):
        if b[i] != -1:
            current_x = a[i] + b[i]
            if xc is None:
                xc = current_x
            else:
                if current_x != xc:
                    posb = False
                    break
    if not posb:
        print(0)
        continue
    
    if xc is not None:
        valid = True
        for i in range(n):
            if b[i] == -1:
                bi = xc - a[i]
                if bi <0 or bi >k:
                    valid = False
                    break
        if valid:
            print(1)
        else:
            print(0)
    else:
        max_a = max(a)
        min_a = min(ai + k for ai in a)
        if max_a <= min_a:
            print(min_a - max_a +1)
        else:
            print(0)
