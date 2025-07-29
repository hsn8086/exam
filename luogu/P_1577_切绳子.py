def checker(lst: list, target: int):
    def warp(lol):
        rst = 0
        for i in lst:
            rst += i // lol
        return rst >= target

    return warp


def bins(check, left, right):
    while left < right:
        ans = (left + right) / 2
        if check(ans):
            left = ans + 0.001
        else:
            right = ans - 0.001
    return left


n, k = map(int, input().split())
lst = [float(input()) for _ in range(n)]


print(bins(checker(lst, k), 0, max(lst)))
