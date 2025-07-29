s=input()
mp={}
for i,v in enumerate(s):
    mp[ord(v)]=i
cnt=0
for i in range(ord("A"),ord("Z")):
    cnt+=abs(mp[i]-mp[i+1])
print(cnt)