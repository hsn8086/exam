from collections import defaultdict


def dfs(e, tag, i):
    if tag[i]:
        return
    else:
        tag[i] = True
    for j in e[i]:
        dfs(e, tag, j)
    # if i-r>=1:
    #     dfs(lst,tag,i-r)
    # if i+r<len(lst):
    #     dfs(lst,tag,i+r)


for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    e = [list() for _ in range(n)]
    for i, v in enumerate(a):
        if i + v < n:
            e[i].append(i + v)
            e[i + v].append(i)
        if i - v > 0:
            e[i].append(i - v)
            e[i - v].append(i)
    tag = [False] * (n)
    cnt = 0
    for i in range(0, n):
        if not tag[i]:
            dfs(e, tag, i)
            cnt += 1
    print(cnt - 1)
