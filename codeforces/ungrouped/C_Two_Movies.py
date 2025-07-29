for _ in range(int(input())):
    n=int(input())
    cnt=0
    lst=[]
    for ai,bi in zip(map(int, input().split()),map(int, input().split())):
        cnt+=ai
        
        lst.append((ai,bi))
    
    for ai,bi in sorted(lst,key=lambda t:(t[0],-t[1])):
        print(ai,bi)
