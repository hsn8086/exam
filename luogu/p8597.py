lst_a=list(map(lambda s: True if s=="*" else False,input()))
lst_b=map(lambda s: True if s=="*" else False,input())
count=0
turn=False
for a,b in zip(lst_a,lst_b):
    if turn:
        a=not a
        turn =False
    if a!=b:
        count+=1
        turn=True

print(count)