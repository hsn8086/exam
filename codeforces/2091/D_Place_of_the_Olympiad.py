from math import ceil


def check(m, req):
    def warp(mid):
        if m // (mid + 1) * mid + m % (mid + 1) >= req:
            return True
        else:
            return False

    return warp


def binary_search(left, right, func):
    ans = -1
    while left <= right:
        mid = (left + right) // 2

        if func(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


for i in range(int(input())):
    n, m, k = map(int, input().split())
    req = ceil(k / n)

    print(binary_search(0, m + 1, check(m, req)))
