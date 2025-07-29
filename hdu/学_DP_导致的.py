def inp_bignum(x):
    if len(x) >= 3:
        return 100
    else:
        return int(x)


for _ in range(int(input())):
    s, k_raw = input().split()
    k = int(k_raw)

    ls = len(set(s))
    if k >= ls:
        print(ls)
    else:
        s = s * k
        dp = [1] * (len(s))
        for i in range(len(s)):
            vi = s[i]
            for j in range(i):
                j = j
                vj = s[j]
                if ord(vi) > ord(vj):
                    dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
