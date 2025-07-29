for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    a = a + [0]

    for i in range(n):
        v = a[i]
        k -= v
        if a[i + 1] > k:
            print(k)
            break
    else:
        print(k)
