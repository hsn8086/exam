import sys
a,b,c,d,x=map(int,sys.stdin.read().split())

tot=0
if x>=a:
    tot+=b
if x>=c:
    tot+=d
print(tot)
