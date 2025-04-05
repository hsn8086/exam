def skip(arr, k):
    n = len(arr)
    is_small = [int(x <= k) for x in arr]
    prefix = [0]
    P = [0]

    for i, val in enumerate(is_small, 1):
        prefix.append(prefix[-1] + val)
        P.append(2 * prefix[i] - i)

    h2 = [False] * (n + 2)
    for i in range(1, n + 1):
        m = n - i + 1
        cnt = prefix[n] - prefix[i - 1]
        if 2 * cnt - m >= m % 2:
            h2[i] = True

    min_p = [float("inf"), float("inf")]

    for r in range(2, n):
        t = r - 1
        parity = t % 2
        min_p[parity] = min(min_p[parity], P[t])
        ok = min_p[r % 2] <= P[r] or min_p[1 - r % 2] <= P[r] - 1
        if ok and h2[r + 1]:
            return True

    return False


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if n == 3:
        print("YES" if sorted(a)[1] <= k else "NO")
        continue

    is_small = [int(x <= k) for x in a]
    prefix = [0]
    P = [0]
    for i, val in enumerate(is_small, 1):
        prefix.append(prefix[-1] + val)
        P.append(2 * prefix[i] - i)

    h = [False] * (n + 2)
    for i in range(1, n + 1):
        m = n - i + 1
        cnt = prefix[n] - prefix[i - 1]
        if 2 * cnt - m >= m % 2:
            h[i] = True

    f1 = [p >= i % 2 for i, p in enumerate(P)]

    any_f1 = False
    skip2 = False
    for j in range(3, n + 1):
        if f1[j - 2]:
            any_f1 = True
        if h[j] and any_f1:
            skip2 = True
            break

    skip1 = skip(a, k)
    skip3 = skip(a[::-1], k)

    print("YES" if skip1 or skip2 or skip3 else "NO")
