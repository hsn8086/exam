import random

t=10000
print(t)
for _ in range(t):
    n=10
    a,b=[],[]
    for _ in range(n):
        a.append(random.randint(1,n))
        b.append(random.randint(1,n))

    print(n)
    print(*a)
    print(*b)