import sys
input = sys.stdin.readline
n,p,k=map(int, input().split())
a=map(int, input().split())
ans=0
for i,v in enumerate(a,1):
    ans+=pow(k,i,p)*pow(v,-1,p)
print(ans)