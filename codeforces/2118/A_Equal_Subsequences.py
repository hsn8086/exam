for _ in range(int(input())):
    n, m = map(int, input().split())
    print("1" * m + "0" * (n - m))
