for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    c = a[: n - 1]
    d = a[n - 1 :]
    rst = sum(d) - sum(c)
    c.append(rst)
    for _ in range(n):
        print(d.pop(), end=" ")
        print(c.pop(), end=" ")

    print(d.pop())
