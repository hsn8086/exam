def check(a, h, x):
    v = 0
    for i in a:
        w = h - i
        if w > 0:
            v += w

    return v - x


def binary_search(a, x, left, right):
    while left < right:
        mid = (left + right + 1) // 2
        if check(a, mid, x) <= 0:
            left = mid
        else:
            right = mid - 1
    return left


ntc = int(input())
for _ in range(ntc):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    result = binary_search(a, x, 1, 2 * 10**9)
    print(result)
