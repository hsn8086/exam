for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if not len(list(filter(lambda x: x >= 0, a))):
        print(max(a))
        continue

    def m(x):
        return max(0, x)

    rst_a = sum(map(m, a[::2]))
    rst_b = sum(map(m, a[1::2]))
    print(max(rst_a, rst_b))
