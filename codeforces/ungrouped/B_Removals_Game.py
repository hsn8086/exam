# ntc=int(input())
# for _ in range(ntc):
#     n=int(input())
#     a=list(map(int,input().split()))
#     b=list(map(int,input().split()))
#     ad={}
#     bd={}
#     for i,t in enumerate(zip(a[:n//2],b[:n//2])):
#         an,bn=t
#         ad[an]=i
#         bd[bn]=i
#     for i,t in enumerate(zip(a[n//2:][::-1],b[n//2:][::-1])):
#         an,bn=t
#         ad[an]=i
#         bd[bn]=i

#     for v,d in ad.items():
#         if bd[v]>ad[v]:
#             print("Alice")
#             break
#     else:
#         print("Bob")
ntc = int(input())
for _ in range(ntc):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if a == b or a[::-1] == b:
        print("Bob")
    else:
        print("Alice")
