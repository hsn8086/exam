from itertools import chain, zip_longest

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(filter(bool, chain.from_iterable(zip_longest(a[::2], b[1::2]))))
    d = list(filter(bool, chain.from_iterable(zip_longest(b[::2], a[1::2]))))
    c_s, d_s = {}, {}
    cnt = 1
    # print(*c)
    # print(*d)
    for i in range(n - 1, -1, -1):
        if c[i] == d[i]:
            cnt = i + 1
            break
        elif c[i] in d_s:
            cnt = i + 1
            break
        elif d[i] in d_s and d_s[d[i]] - i > 1:
            cnt = i + 1
            break
        elif d[i] in c_s:
            cnt = i + 1
            break
        elif c[i] in c_s and c_s[c[i]] - i > 1:
            cnt = i + 1
            break
        if c[i] not in c_s:
            c_s[c[i]] = i
        if d[i] not in d_s:
            d_s[d[i]] = i
    else:
        cnt = 0
    print(cnt)
