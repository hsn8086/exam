import sys

mod = 998244353
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    vis = bytearray(n + 1)
    odd = []
    even = []
    for ptr in range(1, n + 1):
        if vis[ptr]:
            continue
        cnt = 0
        start = ptr
        while not vis[ptr]:
            cnt += 1
            vis[ptr] = 1
            ptr = a[ptr]
        if cnt % 2:
            odd.append(cnt)
        else:
            even.append(cnt)

    le = len(even)
    lo = len(odd)

    cnt = 0
    if lo == 0:
        for length in even:
            tmp = (length // 2) ** 2
            cnt = (cnt + tmp) % mod
        cnt = cnt * pow(2, le - 1, mod) % mod
    elif lo == 2:
        oa, ob = odd
        cnt = oa * ob % mod
        cnt = cnt * pow(2, le, mod) % mod
    else:
        print(1)
        continue

    print(cnt % mod)
