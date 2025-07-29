def max_iv(a):
    max_a = 0
    max_idx = 0
    for i, v in enumerate(a):
        if v > max_a:
            max_a = v
            max_idx = i
    return max_a, max_idx


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k > 1:
        a.sort()
        print(sum(a[-k - 1 :]))
    else:
        max_v, max_i = max_iv(a)

        if max_i == 0:
            print(max_v + max(a[1:]))
        elif max_i == n - 1:
            print(max_v + max(a[:-1]))
        else:
            print(max_v + max(a[0], a[-1]))
