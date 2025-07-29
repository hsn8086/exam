inp=map(int,input().split())
lst=[1,2,3,4,5]
for i in inp:
    lst.remove(i)
print(lst.pop())