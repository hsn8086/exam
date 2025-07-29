mod = 10**9 + 7
for _ in range(int(input())):
    inp = int(input())
    i = inp // 2
    print(i * (i + 1) % mod)
