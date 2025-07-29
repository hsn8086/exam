n=int(input())
a=list(map(int, input().split()))
flag_a=0
flag_b=0
for i in range(1,len(a)-1):
    if a[i-1]<a[i]>a[i+1]:
        if flag_a:
            print(0)
            break
        flag_a=i
    if a[i-1]>a[i]<a[i+1]:
        if flag_b:
            print(0)
            break
        flag_b=i
else:
    print(flag_a*(n-flag_b-1))   