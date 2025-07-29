for _ in range(int(input())):
    n, m, p, q = map(int, input().split())

    if n % p == 0 and (n // p) * q != m:
        print("NO")
    else:
        print("YES")
