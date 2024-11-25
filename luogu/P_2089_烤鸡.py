import itertools

n = int(input())
rst=[]
for a in itertools.product([1, 2, 3], repeat=10):
    if sum(a)==n:
        rst.append(a)

print(len(rst))
for a in rst:
    print(*a)