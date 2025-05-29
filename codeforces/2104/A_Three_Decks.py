for _ in range(int(input())):
    a, b, c = map(int, input().split())
    req_a = b - a
    if c - b < req_a:
        print("NO")
        continue

    a += req_a
    c -= req_a

    if (c - b) % 3 == 0:
        print("YES")
    else:
        print("NO")
