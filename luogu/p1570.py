n, m = map(int, input().split())
lst = []
for v, c in zip(map(int, input().split()), map(int, input().split())):
    lst.append((v, c))
vs,cs=0,0
for i in sorted(lst,key=lambda t:t[0]/t[1])[n-m:]:
    vs+