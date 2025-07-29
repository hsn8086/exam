# from collections import UserList

# class DefaultList(UserList):
#     def __init__(self,func=lambda :None):
#         self.func=func
#         super().__init__()

#     def __getitem__(self,i):
#         if len(self.data)<=i:
#             return self.func()
#         elif i<0 and not self.data:
#             return self.func()

#         return self.data[i]


n = int(input())
prefix = 0
cnt = 0
for e in map(int, input().split()):
    cnt += prefix * e
    prefix += e
print(cnt)
