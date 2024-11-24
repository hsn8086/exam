def clac(a, ans):
    _sum = 0
    for i in a:
        _sum += i // ans

    return _sum


n, k = map(int, input().split())
a = []
_sum = 0
for _ in range(n):
    inp = int(float(input()) * 100)
    _sum += inp
    a.append(inp)


def bisect(func, left, right):
    mid = (right + left) // 2

    if func(mid) > 0:
        left = mid + 1
    else:
        right = mid

    if left == right:
        if func(left):
            return left
        else:
            return left - 1
    return bisect(func, left, right)


print(
    "%.2f" % ((bisect(lambda mid: (clac(a, mid) - k), 0, int(_sum // k) + 10) - 1) // 100)
)
