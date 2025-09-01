from math import isqrt
n=int(input())

for i in range(2,isqrt(n)+2):
    if n%i==0:
        print(n//i)
        break