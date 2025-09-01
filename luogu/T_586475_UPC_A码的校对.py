for _ in range(int(input())):
    a = list(map(int, input().replace("-", "")))
    code = a.pop()
    odd = sum(a[::2])
    even = sum(a[1::2])
    if (10 - (odd * 3 + even) % 10) % 10 == code:
        print("Yes")
    else:
        print("No")
