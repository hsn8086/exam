for _ in range(int(input())):
    n = int(input())
    cnt = (n - 1) * 2 + 1
    print(cnt)
    print(1, 1, n)
    for i in range(1, n):
        print(i + 1, 1, n - i)
        print(i + 1, n - i + 1, n)
