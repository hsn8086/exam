MOD = 998244353
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    prefix = [0]
    suffix = [0]
    for i in a:
        if i == 1:
            prefix.append(prefix[-1] + 1)
        else:
            prefix.append(prefix[-1])

    for i in a[::-1]:
        if i == 3:
            suffix.append(suffix[-1] + 1)
        else:
            suffix.append(suffix[-1])
    suffix = suffix[::-1]
    dp_n = [0]
    for i, v in enumerate(a):
        if v == 2:
            o = prefix[i]
            dp_n.append((dp_n[-1] * 2 + prefix[i]) % MOD)
    idx = 0
    dp_m = [0]
    for i, v in enumerate(a):
        if v == 2:
            idx += 1
            dp_m.append((dp_n[idx - 1] + prefix[i]) * suffix[i] % MOD)

    print(sum(dp_m) % MOD)
