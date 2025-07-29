from math import inf

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    last = inf
    ans = inf
    cnt = 1
    for i in a:
        if last == i:
            cnt += 1
        else:
            ans = min(ans, (n - cnt) * last)
            last = i
            cnt = 1
    ans = min(ans, (n - cnt) * last)
    print(ans)
