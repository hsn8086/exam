m = int(input())
rst=[]
for n in range(2, int((2 * m) ** 0.5) + 1):
    l = (m - n * (n - 1) // 2) / n
    if l >= 1 and l == int(l):
        l = int(l)
        r = l + n - 1
        rst.append((l,r))
rst.sort(key=lambda x:x[0])
for l,r in rst:
    print(l,r)
"""
((l+r)*(r-l+1))/2=m
(l+r)*(r-l+1)=2m
lr-l2+l+r2-lr+r=2m
-l2+l+r2+r-2m=0
l-l2=2m-r2-r
a=-1
b=1
c=r2+r-2m
l=(-1+sqrt(1+4*(r2+r-2m)))/(2*(-1))
"""
