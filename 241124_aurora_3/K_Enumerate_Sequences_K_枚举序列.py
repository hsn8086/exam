from itertools import product
def check(a_rst,a_r,k):

    for i in range(len(a_rst)):
        if a_rst[i]>a_r[i]:
            return False
    if sum(a_rst)%k!=0:
        return False
    return True
n,k=map(int,input().split())
a=list(map(int,input().split()))
max_r=max(a)

for a_rst in product(range(1,max_r+1),repeat=n):

    if check(a_rst,a,k):
        print(" ".join(map(str,a_rst)))