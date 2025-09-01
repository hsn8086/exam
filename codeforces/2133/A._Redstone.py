from itertools import pairwise
# print(input())
for _ in range(int(input())):
    n=int(input())
    a=sorted(map(int,input().split()))
    for x,y in pairwise(a):
        if x==y:
            print("YES")
            break
        print()
    else:
        print("NO")
    