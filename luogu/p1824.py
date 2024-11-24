def check(a: list[int], ans: int, c: int):
    ptr = 0
    last = float("-inf")
    while c:
        if ptr >= len(a):
            break
        if a[ptr] - last >= ans:
            c -= 1
            last = a[ptr]
        ptr += 1
    else:
        return True
    return False


n, c = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()


def bisect(func, left, right):
    mid = (right + left) // 2

    if func(mid):
        left = mid + 1
    else:
        right = mid

    if left == right:
        if func(left):
            return left
        else:
            return left - 1
    return bisect(func, left, right)


print(bisect(lambda mid: check(a, mid, c), 0, int((1e9) // c)))
