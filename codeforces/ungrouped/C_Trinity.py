for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    b = [sum(i) for i in zip(a[1:], a[:-1])]
    left = 0
    right = 2
    rst = n - 2
    while right < n:
        while a[right] - b[left] >= 0 and right - left >= 2:
            left += 1
        rst = min(rst, n - (right - left + 1))
        right += 1
    print(rst)
