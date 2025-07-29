from collections import defaultdict

n = int(input())
mp = defaultdict(list)
for i, v in enumerate(map(int, input().split()), 1):
    mp[v].append(i)

ans = -1
max_i = 0
for i, lst in mp.items():
    if len(lst) == 1:
        if max_i < i:
            ans = lst[0]
            max_i = i
print(ans)
