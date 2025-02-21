def isqrt_newton(n):
    x = 1
    decreased = False
    while True:
        nx = (x + n // x) // 2
        if x == nx or (nx > x and decreased):
            break
        decreased = nx < x
        x = nx
    return x


n = int(input())
for _ in range(n):
    k = int(input())
    l, r = k, 2 * 10**18
    while l < r:
        mid = (l + r) // 2
        if mid - isqrt_newton(mid) < k:
            l = mid + 1
        else:
            r = mid
    print(l)
