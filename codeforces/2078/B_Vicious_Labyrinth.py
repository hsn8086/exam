for _ in range(int(input())):
    n, k = map(int, input().split())

    if k % 2 == 1:
        to = n
    else:
        to = n - 1

    print(*(to for _ in range(n - 2)), n, n - 1)
