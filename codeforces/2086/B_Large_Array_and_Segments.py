# import bisect
# for _ in range(int(input())):
#     n,k,x=map(int, input().split())
#     a=map(int, input().split())
#     prefix=[0]
#     for i in a:
#         prefix.append(prefix[-1]+i)
#     for i in range(1,len(prefix)):
#         v=prefix[-1]-prefix[-i]
    
#         last=(x-v)%prefix[-1]
#         idx=bisect.bisect(prefix,last)


import bisect
for _ in range(int(input())):
    n,k,x=map(int, input().split())
    a=map(int, input().split())
    prefix=[0]
    for i in a:
        prefix.append(prefix[-1]+i)
    x2,rk=x%prefix[-1], x//prefix[-1]

    cnt=0
    for i in range(1,len(prefix)+1):
        v=prefix[-1]-prefix[-i]
        if v>=x2:
            cnt+=1
    print(max(0,cnt+(k-rk-1)*n))