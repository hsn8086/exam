# from collections import deque
# from dataclasses import dataclass
# @dataclass
# class Node:
#     next: "Node"=None
#     value: int
# ntc=int(input())
# for _ in range(ntc):
#     n=int(input())
#     a=map(int,input().split())
#     first=None
#     last=None
#     for i in a:
#         nd=Node(value=i)
#         if last is not None:
#             last.next=nd
#         else:
#             first = nd
#         last=nd

#     flag=True
#     while flag:
#         nd=first
#         while nd.next.next:
#             nd=nd.next
#             ndn=nd.next
#             if nd.value>ndn.value:

def ext(a:list):
    flag = True
    app_lst = []
    while flag:
        i = 0

        flag = False
        while i < len(a) - 1:
            if a[i] > a[i + 1]:
                value = a.pop(i)
                app_lst.append(value + 1)
                flag = True
            else:
                i += 1
    return a,app_lst
# ntc = int(input())
# for _ in range(ntc):
#     n = int(input())
#     a = list(map(int, input().split()))
#     flag = True
#     app_lst=[0]
#     while app_lst:
#         a,app_lst=ext(a)
#         app_lst.sort()
#         a.extend(app_lst)
#     print(" ".join(map(str, a)))


ntc = int(input())
for _ in range(ntc):
    n = int(input())
    a = list(map(int, input().split()))
    flag = True
    app_lst=[]

    i=0
    
    flag = True
    a,app_lst = ext(a)
    min_=min(app_lst+[float("+inf")])
    # while flag:
    #     flag=False
    #     while i < len(a) - 1:
    #         if a[i] > a[i + 1]:
    #             value = a.pop(i)
    #             app_lst.append(value + 1)
    #             min_=min(min_,value + 1)
    #             flag=True
    #         else:
    #             i += 1
    
    while i < len(a):
        if a[i]>min_:
            value = a.pop(i)
            app_lst.append(value + 1)
            min_=min(min_,value + 1)
        else:
            i += 1
    app_lst.sort()
    a.extend(app_lst)
    print(" ".join(map(str, a)))