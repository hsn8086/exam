from collections import defaultdict

for _ in range(int(input())):
    act = defaultdict(lambda: -1)
    ans_act = set()
    last_z = 0
    n = int(input())
    a = list(map(int, input().split()))
    pre = [0] * (n + 1)
    cnt = 0
    for i, v in enumerate(a):
        pre[i] = len(ans_act)
        if v == 0:
            last_z = i
        elif act[v] == -1:
            act[v] = i
        elif last_z > act[v]:
            ans_act.add(v)

    rst = [0] * (10**6 + 10)
    for i, v in enumerate(a):
        if v != 0:
            rst[v] = max(rst[v], pre[i])
    print(sum(rst))

