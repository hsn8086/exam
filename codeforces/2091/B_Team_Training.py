# from math import ceil

# for _ in range(int(input())):
#     n, x = map(int, input().split())
#     a = sorted(map(int, input().split()), reverse=True)
#     lst = [0] * 10**5
#     max_ = 0
#     for i in a:
#         v = ceil(x / i)
#         if v >= 10**5:
#             break
#         lst[v - 1] += 1
#         max_ = max(max_, v + 10)
#     ans = 0
#     for i_, v in enumerate(lst):
#         if i_>max_:
#             break
#         i = i_ + 1
#         pans, nex = divmod(v, i)
#         ans += pans
#         if nex and len(lst) < i:
#             lst[i_ + 1] += nex
#     print(ans)
from math import ceil

for _ in range(int(input())):
    n, x = map(int, input().split())
    a = sorted(map(int, input().split()), reverse=True)
    cnt=0
    rst=0
    for i in a:
        cnt+=1
        if cnt*i>=x:
            rst+=1
            cnt=0
    print(rst)