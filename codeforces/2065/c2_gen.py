import random
import subprocess
t=1*(10**4)
tc=[]
print(t)
for _ in range(t):
    n=random.randint(1,10**5)
    m=random.randint(1,10**5)
    
    a=(random.randint(1,10**9) for _ in range(n))
    b=(random.randint(1,10**9) for _ in range(m))
    print(n,n)
    print(*a)
    print(*b)





