# from itertools import permutations


# def sol(a, b, c):
#     if (c - b) % a == 0:
#         return int((c - b) / a)
#     else:
#         return -1


# for _ in range(int(input())):
#     ans = []
#     for _ in range(int(input())):
#         a = list(map(int, input().split()))
#         rsts = [sol(a, b, c) for a, b, c in permutations(a, 3)]
#         rst = list(filter(lambda x: x != -1, rsts))
#         pl = []
#         if ans:
#             for i in ans:
#                 if i not in rst:
#                     pl.append(i)
#             for i in pl:
#                 ans.remove(i)
#             if len(ans) == 1:
#                 print(ans[0])
#         else:
#             ans = rst

#     print(ans[0])
from itertools import permutations


def sol(a, b, c):
    if (c - b) % a == 0 and (c - b) / a >= 0:
        return int((c - b) / a)
    else:
        return -1


for _ in range(int(input())):
    ans = []
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        rsts = filter(
            lambda x: x != -1, (sol(a, b, c) for a, b, c in permutations(a, 3))
        )
        if ans:
            rsts = filter(lambda x: x in ans, rsts)
            ans = list(rsts)
            if len(ans) == 1:
                print(ans[0])
                break
        else:
            ans = list(rsts)

    else:
        print(ans[0])
