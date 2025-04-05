from random import shuffle
for _ in range(int(input())):
    n=int(input())
    lst=[]
    for _ in range(n-1):
        lst.append(next(map(int, input().split())))
    lst.extend(map(int, input().split()))
    lst_cp=lst.copy()
    shuffle(lst_cp)
    st=set(lst_cp)

    for i in range(1,2*n+1):
        if i not in st:
            lst=[i]+lst
            break
    print(*lst)