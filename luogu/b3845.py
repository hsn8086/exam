import math
def issq(num):
    return int(math.sqrt(num))**2==num
n=int(input())
count=0
for c in range(5,n+1):
    for b in range(1,int(c*math.sqrt(2)/2)+1):
        a=c**2-b**2
        if issq(a):
            # print(math.sqrt(a),b,c)
            count+=1
print(count)

"""
a=c*sqrt(2)/2
"""