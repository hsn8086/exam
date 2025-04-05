
def skip1(arr, k):
        N = len(arr)
        sm = [int(x <= k) for x in arr]
        pr = [0] * (N + 1)
        PP = [0] * (N + 1)
        for i in range(1, N + 1):
            pr[i] = pr[i - 1] + sm[i - 1]
            PP[i] = 2 * pr[i] - i

        h2 = [False] * (N + 2)
        for i in range(1, N + 1):
            m = N - i + 1
            cnt = pr[N] - pr[i - 1]
            val = 2 * cnt - m
            if val >= m % 2:
                h2[i] = True

        INF = float('inf')
        mn = [INF, INF]

        for r in range(2, N):
            t = r - 1
            mn[t % 2] = min(mn[t % 2], PP[t])
            prr = PP[r]
            ok = False
            if mn[r % 2] <= prr:
                ok = True
            if mn[1 - r % 2] <= prr - 1:
                ok = True
            if ok and h2[r + 1]:
                return True
        return False


for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))

    if n == 3:
        b = sorted(a)
        print( "YES" if b[1] <= k else "NO")
        continue

    small = [int(x <= k) for x in a]
    pre = [0] * (n + 1)
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + small[i - 1]
        p[i] = 2 * pre[i] - i

    h = [False] * (n + 2)
    for i in range(1, n + 1):
        m = n - i + 1
        cnt = pre[n] - pre[i - 1]
        val = 2 * cnt - m
        if val >= m % 2:
            h[i] = True

    f1 = [False] * (n + 1)
    for i in range(1, n + 1):
        if p[i] >= i % 2:
            f1[i] = True

    skip2 = False
    any_f1 = False
    for j in range(3, n + 1):
        if f1[j - 2]:
            any_f1 = True
        if h[j] and any_f1:
            skip2 = True
            break

    skip1 = skip1(a, k)
    skip3 = skip1(list(reversed(a)), k)

    print("YES" if skip1 or skip2 or skip3 else "NO")


