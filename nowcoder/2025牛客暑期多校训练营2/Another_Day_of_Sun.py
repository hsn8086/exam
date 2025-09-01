import sys

mod = 998244353
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    dp_1 = [0]
    dp_0 = [0]
    dpc_0 = [1]
    dpc_1 = [0]
    for i in a:
        if i == -1:
            z, o = dp_0[-1] + dp_1[-1], dp_0[-1] + dpc_0[-1] + dp_1[-1]
            c = (dpc_0[-1] + dpc_1[-1]) % mod
            dp_0.append(z % mod)
            dp_1.append(o % mod)
            dpc_0.append(c)
            dpc_1.append(c)
        elif i == 1:
            dp_1.append((dp_0[-1] + dpc_0[-1] + dp_1[-1]) % mod)
            dp_0.append(0)
            dpc_1.append((dpc_0[-1] + dpc_1[-1]) % mod)
            dpc_0.append(0)

        elif i == 0:
            dp_0.append((dp_0[-1] + dp_1[-1]) % mod)
            dp_1.append(0)

            dpc_0.append((dpc_0[-1] + dpc_1[-1]) % mod)
            dpc_1.append(0)
    # print(dpc_0)
    # print(dpc_1)
    # print(dp_0)
    # print(dp_1)
    # print()
    print((dp_0[-1] + dp_1[-1]) % mod)
