for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    if k == 0:
        for i, j in zip(s, s[::-1]):
            if ord(j) > ord(i):
                print("YES")
                break
            elif ord(j) < ord(i):
                print("NO")
                break
        else:
            print("NO")
    else:
        if min(map(ord, s))< max(map(ord, s)):
            print("YES")
        else:
            print("NO")
