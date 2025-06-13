for _ in range(int(input())):
    n = int(input())
    a = list(range(1, n + 1))

    print(*a[::2], *a[1::2][::-1])
