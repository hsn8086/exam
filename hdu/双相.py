for _ in range(int(input())):
    n = int(input())
    r = []
    b = []
    for v, t in zip(map(int, input().split()), input()):
        if t == "R":
            r.append(v)
        else:
            b.append(v)
    r.sort(reverse=True)
    b.sort(reverse=True)
    if len(r)>len(b):
        i=len(b)
        print(sum(r[:i+1]) + sum(b[:i]))
    else:
        i=len(r)
        print(sum(r[:i]) + sum(b[:i]))
    
