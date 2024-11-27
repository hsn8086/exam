def clac(a, c, w):

    sum_ = 0
    for s in a:
        sum_ += (s + 2 * w) ** 2
    return sum_ - c


def bis(fun, lo, ro):
    mid = (lo + ro) // 2
    v = fun(mid)
    if v > 0:
        return bis(fun, lo, mid - 1)
    elif v < 0:
        return bis(fun, mid + 1, ro)
    else:
        return mid


ntc = int(input())
for _ in range(ntc):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))

    w = bis(lambda x: clac(a, c, x), 0, 10**9)
    print(w)
    # print(clac(a,c,w))
