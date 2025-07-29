cnt=0
login=False
for _ in range(int(input())):
    cmd=input()
    if cmd=="login":
        login=True
    elif cmd=="logout":
        login=False
    
    if not login and cmd=="private":
        cnt+=1

print(cnt)