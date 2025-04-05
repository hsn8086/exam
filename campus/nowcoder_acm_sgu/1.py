last=""
flag=False
for _ in range(int(input())):
    if flag:
        print(last)
        continue
    s=input()
    if last==s:
        flag=True
    last=s
    print(s)